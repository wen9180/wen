var rule = {
    模板: '采集1',
    title: '极速资源',
    host: 'https://jszyapi.com',
    //homeTid: '13',
    cate_exclude: '电影片|连续剧|综艺片|动漫片|电影解说|伦理片|演员|新闻资讯|电视剧|电影|综艺|动漫',
    parse_url: '',
搜索: `js:
        let d = [];
        // 忽略分类
        let cate_exclude = '8';
        let html = request(input);
        let list = JSON.parse(html).list;
        list.forEach(function (it){
            if(!cate_exclude.match(it.type_id)){
                d.push({
                    title:it.vod_name,
                    img:it.vod_pic,
                    desc:it.vod_remarks,
                    url:it.vod_id
                });
            }
        });
        setResult(d);
    `}