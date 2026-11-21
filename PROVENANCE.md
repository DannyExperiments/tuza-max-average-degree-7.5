# Snapshot provenance

Three Git commits identify the source snapshots. Each row gives the SHA-256 digest of the exact manifest bytes retrieved at that commit. **The first two manifests have verified Bitcoin attestations.** At 19:20 UTC on 21 November 2026, all three calendars for the third manifest still reported that Bitcoin confirmation was pending.

| Snapshot | Git content commit | Manifest | SHA-256 of manifest | Bitcoin block and header time, 21 November 2026 |
| --- | --- | --- | --- | --- |
| 1 | `58b72b7882928d9ca966b8dc8f992cf35380a4e1` | `MANIFEST.sha256` | `cded3cb40dbda9bb569bc35341b1bcaef051393fd10177952ae35b1f23c190f8` | [976849](https://blockstream.info/block/0000000000000000000149beb996e259355fe05c4c5c61b2978a209aadc23368) · 05:09:19 UTC |
| 2 | `97cb280cfb734b223bbc2773d21919e060700469` | `MANIFEST-2.sha256` | `d6773246f469d00b2f597e207a3d3329946c56b81f061a8252989765f1b2a142` | [976886](https://blockstream.info/block/00000000000000000000e5057a0532d66840d6474b739205c3201b8d33339577) · 10:38:35 UTC |
| 3 | `14689c300642eeb8f3c72f4a16f319dc8cf63e05` | `MANIFEST-3.sha256` | `c893952ede0df01aaf8bb0d664f8229c07fc0c33bc81309b6d6858c069241274` | Pending at the stated check |

The complete detached receipts were retrieved at timestamp-maintenance commit `80ca9d8eb6758c6015ae76c1b120244e0bec88ed`. Each receipt’s starting digest matched the SHA-256 of the corresponding manifest. The verification followed every Bitcoin branch to the block’s transaction Merkle root, recalculated the double-SHA-256 block ID, and checked its proof of work against the difficulty target encoded in the header. Blockstream and mempool.space supplied identical 80-byte headers at all five distinct heights. Block times above are the miner-reported header times. [OpenTimestamps verification format](https://github.com/opentimestamps/python-opentimestamps/blob/8c3dc6fbdf6fcba054e78643e9df5eccd8c9fce4/opentimestamps/core/notary.py) · [Block header interface](https://github.com/Blockstream/esplora/blob/master/API.md#bitcoin-endpoints)

| Released receipt | What can be checked | SHA-256 of released receipt |
| --- | --- | --- |
| [Snapshot 1](evidence/timestamps/MANIFEST.sha256.ots) | One complete branch to block 976849. Two further branches in the source receipt verified at heights 976851 and 976858. | `8494283c1d057d6fccc79b19e46bd0314a2bd1427f0e5e96937d6af605770934` |
| [Snapshot 2](evidence/timestamps/MANIFEST-2.sha256.ots) | One complete branch to block 976886. The source receipt has a second branch to that block and a third to 976912. All three verified. | `820c9190d42c4077bae3f37b7e9aa6963d1e0d22e662f333e2c3323918e07484` |
| [Snapshot 3](evidence/timestamps/MANIFEST-3.sha256.ots) | The original 724-byte receipt contains pending commitments with Alice, Bob and Finney. A read-only lookup of each commitment returned “Pending confirmation in Bitcoin blockchain.” | `5dae9ae2afaf72c13902a2bc1566fa41723e2537c192f8fe9da4ba2b3dc31265` |

From the release root, the following commands verify the two confirmed receipts against the published digests with an existing OpenTimestamps client and a synchronized Bitcoin Core node. The third command displays the third receipt’s recorded branches. [OpenTimestamps client](https://github.com/opentimestamps/opentimestamps-client/blob/f3a9e92e4dcb89ed93396d71ec808b3290a438c4/README.md)

```sh
ots verify -d cded3cb40dbda9bb569bc35341b1bcaef051393fd10177952ae35b1f23c190f8 evidence/timestamps/MANIFEST.sha256.ots
ots verify -d d6773246f469d00b2f597e207a3d3329946c56b81f061a8252989765f1b2a142 evidence/timestamps/MANIFEST-2.sha256.ots
ots info evidence/timestamps/MANIFEST-3.sha256.ots
```

A Bitcoin attestation dates a commitment to the manifest digest. Establishing that a particular manuscript or verification file occurred in a snapshot also requires its corresponding manifest entry and matching file bytes. Mathematical correctness and historical priority require separate evidence.
