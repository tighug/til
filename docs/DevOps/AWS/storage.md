# Storage

## EBS

Elastic Block Store (EBS)は、EC2 インスタンスにアタッチして利用できるブロックレベルのストレージサービスです。1 つのボリュームは最大で**16TB**です。実際に保存された容量ではなく、確保した容量分の課金が発生します。

### ボリュームタイプ

| Volume Type                   | Disk | Description |
| ----------------------------- | ---- | ----------- |
| 汎用 SSD（gp2）               | SSD  |             |
| プロビジョン度 IOPS（io1）    | SSD  |             |
| スループット最適化 HDD（st1） | HDD  |             |
| コールド HDD（sc1）           | HDD  |             |
| マグネティック                | HDD  |             |

### スナップショット

## S3

Simple Storage Service (S3)は、オブジェクトストレージサービスです。

### ストレージクラス

-   S3 標準
-   S3 Intelligent-Tiering
-   S3 標準 - 低頻度アクセス
-   S3 1 ゾーン - 低頻度アクセス
-   S3 Glacier

## Storage Gateway

**Storage Gateway**は、オンプレミスから AWS のストレージサービスへのアクセスを可能にする仮想アプライアンスです。

-   ファイルゲートウェイ
-   テーブゲートウェイ
-   保管型ボリュームゲートウェイ
-   キャッシュ型ボリュームゲートウェイ

## EFS

Elastic File System（**EFS**）は、ファイル共有ストレージのマネージドサービスです。
