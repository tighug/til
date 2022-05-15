# ERC 721

もっとも広く使われている代替不可能トークン（NFT：Non-Fungible Token）。似たようなものに Multi-Fungible Token の ERC721x がある。

## ERC721

| method                                                        | return  | description                                                                                  |
| ------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------- |
| `balanceOf(address owner)`                                    | uint256 | アカウントが所有する NFT の量                                                                |
| `ownerOf(uint256 tokenId)`                                    | address | `tokenId`で指定された NFT の所有者のアドレス                                                 |
| `safeTransferFrom(address from, address to, uint256 tokenId)` | void    | 特定の NFT を転送する                                                                        |
| `transferFrom(address from, address to, uint256 tokenId)`     | void    | 特定の NFT を転送する（上記推奨）                                                            |
| `approve(address to, uint256 tokenId)`                        | void    | NFT を転送するために別のアドレスを承認する。トークン所有者またはオペレータ飲みが呼び出し可能 |
| `getApproved(uint256 tokenId)`                                | address | NFT の承認済みアドレス                                                                       |
| `setApprovalForAll(address operator, bool approved)`          | void    | 特定のオペレータの承認を設定（true）・解除（false）する                                      |
| `isApprovedForAll(address owner, address operator)`           | bool    | オペレータが特定の所有者によって承認されているか                                             |

| event                                                            | description |
| ---------------------------------------------------------------- | ----------- |
| `Transfer(address from, address to, uint256 tokenId)`            |             |
| `Approval(address owner, address approved, uint256 tokenId)`     |             |
| `ApprovalForAll(address owner, address operator, bool approved)` |             |

## ERC721Mintable (Extension)

ERC20 バージョンのように、新しいトークンを鋳造できる。

| modifier       | description |
| -------------- | ----------- |
| `onlyMinter()` |             |

| methods                             | return | description        |
| ----------------------------------- | ------ | ------------------ |
| `mint(address to, uint256 tokenId)` | bool   | トークンを鋳造する |
| `isMinter(address)`                 |        |                    |
| `addMinter(address)`                |        |                    |
| `renounceMinter()`                  |        |                    |

| event                    | description |
| ------------------------ | ----------- |
| `MinterAdded(address)`   |             |
| `MinterRemoved(address)` |             |

## ERC721Burnable (Extension)

ERC777 バージョンのように、トークンを破壊できる。

| methods               | return | description           |
| --------------------- | ------ | --------------------- |
| burn(uint256 tokenId) | void   | 特定の NFT を破壊する |
