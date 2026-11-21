"""Render the README animation from the two fans in the interactive figure."""

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFont

from check_figure import VISUALS, ViewerHTML, viewer_fans


WIDTH, HEIGHT, SCALE = 760, 292, 2
PAPER = "#faf9f4"
INK = "#152e32"
LINES = ("#a3441d", "#305ba6", "#286760")
FILLS = ("#e6a16f", "#8eadd9", "#72a79e")


def scaled(xy):
    return tuple(round(SCALE * value) for value in xy)


def project(point, yaw, tilt, center):
    x, y, z = point
    horizontal = x * math.cos(yaw) - z * math.sin(yaw)
    forward = x * math.sin(yaw) + z * math.cos(yaw)
    up = y * math.cos(tilt) - forward * math.sin(tilt)
    depth = y * math.sin(tilt) + forward * math.cos(tilt)
    return center + 80 * horizontal, 164 - 80 * up, depth


def dashed_line(draw, start, end, color):
    x, y = start
    dx, dy = end[0] - x, end[1] - y
    length = math.hypot(dx, dy)
    for begin in range(0, math.ceil(length), 12):
        finish = min(begin + 7.5, length)
        ends = [(x + dx * step / length, y + dy * step / length) for step in (begin, finish)]
        draw.line([scaled(p) for p in ends], fill=color, width=3*SCALE)


def render(vertices, fans, rims, phase, fonts):
    image = Image.new("RGB", scaled((WIDTH, HEIGHT)), PAPER)
    draw = ImageDraw.Draw(image, "RGBA")
    draw.line([scaled((WIDTH/2, 14)), scaled((WIDTH/2, HEIGHT-13))], fill="#cbd5d0", width=SCALE)
    yaw = -0.55 + 0.63 * math.sin(phase)
    tilt = 0.53 + 0.12 * math.sin(phase - 0.45)
    for index, (edges, faces) in enumerate(fans):
        center = (index + 0.5) * WIDTH/2
        points = {v: project(xyz, yaw, tilt, center) for v, xyz in vertices.items()}

        def depth(mark):
            return sum(points[v][2] for v in mark) / len(mark)

        title = ("First fan", "Second fan")[index]
        draw.text(scaled((center, 23)), title, font=fonts["title"], fill=LINES[index], anchor="mm")
        draw.text(scaled((center, 46)), "Rim  " + " - ".join(rims[index]),
                  font=fonts["rim"], fill=INK, anchor="mm")

        other_edges, other_faces = fans[1-index]
        for face in sorted(faces, key=lambda face: (depth(face), face)):
            color = FILLS[2 if face in other_faces else index]
            draw.polygon([scaled(points[v][:2]) for v in face], fill=(*ImageColor.getrgb(color), 83))
        for edge in sorted(edges, key=lambda edge: (depth(edge), edge)):
            ends = [points[v][:2] for v in edge]
            kind = 2 if edge in other_edges else index
            if kind == 1:
                dashed_line(draw, *ends, LINES[kind])
            else:
                draw.line([scaled(p) for p in ends], fill=LINES[kind], width=(4 if kind == 0 else 2)*SCALE)
        for label in sorted(points, key=depth):
            x, y, _ = points[label]
            draw.ellipse([scaled((x-3.5, y-3.5)), scaled((x+3.5, y+3.5))],
                         fill=PAPER, outline=INK, width=2*SCALE)
            dx = 0 if label == "a" else (-11 if x < center else 11)
            dy = -12 if label == "a" or y < 171 else 11
            draw.text(scaled((x+dx, y+dy)), label, font=fonts["label"], anchor="mm",
                      fill=INK, stroke_width=SCALE, stroke_fill=PAPER)
    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=VISUALS / "high-fans-rotation.gif")
    args = parser.parse_args()
    viewer = VISUALS / "high-fans.html"
    fans = viewer_fans(viewer)
    html = ViewerHTML()
    html.feed(viewer.read_text(encoding="utf-8"))
    html.close()
    data = json.loads("".join(html.scripts["data"]))
    fonts = {role: ImageFont.load_default(size=size*SCALE)
             for role, size in (("title", 22), ("rim", 15), ("label", 17))}
    count = 48
    frames = [render(data["vertices"], fans, data["rims"], 2*math.pi*i/count, fonts)
              for i in range(count)]
    sample = Image.new("RGB", (WIDTH, HEIGHT*4))
    for i, frame in enumerate(frames[::count//4]):
        sample.paste(frame, (0, HEIGHT*i))
    palette = sample.quantize(colors=64)
    accents = [channel for color in (PAPER, INK, *LINES) for channel in ImageColor.getrgb(color)]
    palette.putpalette(accents + palette.getpalette()[:64*3])
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(args.output, save_all=True, append_images=indexed[1:], duration=100,
                    disposal=1, loop=0, optimize=False)


if __name__ == "__main__":
    main()
