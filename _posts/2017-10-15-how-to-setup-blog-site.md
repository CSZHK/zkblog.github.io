---
layout: post
title: 个人博客站点搭建
date: 2017-10-15
categories: blog
tags: [经验,教程,知识管理]
description: 开博第一篇。

---

#### 用了一上午搭建了个人站点，简要做了记录如下，默认会使用GitHub

- 域名购买
- DNS注册
- GitHub Pages搭建

# 域名购买

1.我用的是[GoDaddy](https://sg.godaddy.com/zh?cvosrc=ppc.baidu.Title&matchtype=Exact&mkwid=OdF1WcMU_pkw_Title_pmt_Exact_&isc=GPPTDOD100) ，注册好账户，登录
![](http://upload-images.jianshu.io/upload_images/726103-f22c2803cc651fcd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)     *GoDaddy首页*

2.搜索你想要的域名，加入购物车购买，可以在网上搜索优惠券打折，支持支付宝付款
![](http://upload-images.jianshu.io/upload_images/726103-50a1aa42e121e3cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) *搜索域名*

![](http://upload-images.jianshu.io/upload_images/726103-f663fb35d33ec895.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*去掉无用的捆绑*

![](http://upload-images.jianshu.io/upload_images/726103-5b192deff8e8b04f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*选择年限并付款*

3.[修改域名DNS服务器指引](https://cloud.tencent.com/document/product/302/5518) ，使用DNSpod的DNS域名解析服务。
![](http://upload-images.jianshu.io/upload_images/726103-5b7a954ae98d4f37.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*进入DNS管理*

![](http://upload-images.jianshu.io/upload_images/726103-295323f0921cd97d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*使用DNSpod的DNS域名服务器*

# DNS注册

1.使用[DNSpod](https://www.dnspod.cn/)，可以使用微信登陆
![](http://upload-images.jianshu.io/upload_images/726103-992e41f896b9f07f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*登陆以后进入管理控制台*

2.注册域名
![](http://upload-images.jianshu.io/upload_images/726103-6a0bc0c5ce4196c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) *域名注册*

![](http://upload-images.jianshu.io/upload_images/726103-a9fc9087c2994d8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*添加一级域名为购买的域名*

3.域名解析
![](http://upload-images.jianshu.io/upload_images/726103-d7f61344b796019a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*进入域名解析*

![](http://upload-images.jianshu.io/upload_images/726103-407376b94482f545.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*添加A类型的记录*

添加A类型的记录，记录值为192.30.252.154和192.30.252.153，这两个ip地址是github pages服务为我们提供的接口，www和@子域必须配置，否则不成功。配置时要看下是否有更改
（[help.github.com/articles/setting-up-an-apex-domain/](https://help.github.com/articles/setting-up-an-apex-domain/)）。
![](http://upload-images.jianshu.io/upload_images/726103-8710769d62fecc91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*GitHub Pages 服务ip*

# GitHub Pages搭建

[操作前简单了解下原理](https://pages.github.com/) 
1.fork博客模板
访问[github.com/cnfeat/blog.io](https://github.com/cnfeat/blog.io) ，fork代码
![](http://upload-images.jianshu.io/upload_images/726103-d75573b20a7bf81e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*fork到自己的repository*

2.修改fork下来的repository的名称为：GitHub昵称.GitHub.io
![](http://upload-images.jianshu.io/upload_images/726103-2c7818266103074d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*GitHub昵称.GitHub.io*

 3.修改CNAME文件的配置为自己购买的域名
![](http://upload-images.jianshu.io/upload_images/726103-0e0dea147ca2418d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)*修改域名*

稍等几分钟后，浏览器访问 GitHub昵称.GitHub.io或者zhukang.life（自己的域名），就会看到博客首页了。

---
