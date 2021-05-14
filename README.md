## Deprecated
目前我几乎不再使用 Fedora Linux ，精力有限，不再维护本项目。 https://copr.fedorainfracloud.org 有维护者提供较新版本。


# 网易云音乐 RPM 包
当前状态：Fedora 23/24 下安装后可以正常打开使用。

## 安装
1. 安装 RPM Fusion 源 (free): http://rpmfusion.org/Configuration
2. 终端下执行：
    
    ```
    wget https://dl.senorsen.com/pub/package/linux/add_repo.sh -qO - | sudo sh
    sudo dnf install http://dl-http.senorsen.com/pub/package/linux/rpm/senorsen-repo-0.0.1-1.noarch.rpm
    # 上一步成功后
    sudo dnf install netease-cloud-music
    ```
    注意：该命令会下载一个 30+MB 的 RPM ，所以可能比较缓慢。
3. 安装完成后，在 Dash 中搜索 netease，即可看到网易云音乐的图标。

重要提醒：
安装后会安装我的 RPM 源，以供之后随源更新。如果不需要，可以手动删除，或者自己 clone 本仓库后修改打包脚本。

## 依赖
- Fedora 23/24
- RPMFusion (free)
