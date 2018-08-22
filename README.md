# helm-charts-mirror


kubernetes helm 国内镜像，使用Travis CI每天自动同步。[![Sync Status](https://travis-ci.org/Doublemine/helm-charts-mirror.svg?branch=sync)](https://travis-ci.org/Doublemine/helm-charts-mirror)

Helm官方charts仓库托管在GCP上，国内由于众所周知的原因，国内集群无法访问。因此采用travis自动同步至GitHub pages以作为国内镜像使用。


# 使用方法:


```bash
helm repo add stable https://doublemine.github.io/helm-charts-mirror/
```

# 致谢：


Python同步脚本引用至[@BurdenBear](https://github.com/BurdenBear/kube-charts-mirror)，并做了少许修改。