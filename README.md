# 网易云音乐 rpm包
当前状态：Fedora 23/24 下安装后可以正常打开，测试中播放音乐等功能均可用。

理论上 openSUSE 也能用，但未测试。

## 安装
1. 安装 RPM Fusion 源 (free) ：http://rpmfusion.org/Configuration (openSUSE 用户：不清楚安装这个源会不会导致一些依赖关系混乱，欢迎反馈)
2. 终端下执行：
    
    ```
    sudo dnf install http://dl-http.senorsen.com/pub/package/linux/rpm/senorsen-repo-0.0.1-1.noarch.rpm
    # 上一步成功后
    sudo dnf install netease-cloud-music
    ```
    注意：该命令会下载一个30+MB的rpm，所以可能比较缓慢。
3. 安装完成后，在 Dash 中搜索 netease，即可看到网易云音乐的图标（与其他 Ubuntu、Debian 系统安装后使用方法无异）。
4. 使用正常吗？如果能用请给个 star >\_< ，如果使用不正常，请在 Issue 里发一下发行版、版本、截图~

重要提醒：
安装后会安装我的 rpm repo 源，以供之后随源更新。如果不需要，可以手动删除，或者自己 clone 本仓库后修改打包脚本。

## 依赖
Fedora 23/24 , RPMFusion (free)
 
## Copyright
网易云音乐是网易公司的注册商标，本repo与网易公司没有任何关系。

## Author
打包脚本： Senorsen <senorsen.zhang@gmail.com>

网易云音乐忠实用户。

