var rule={
			title: '第一动漫',
            host: 'https://1anime.me',
            // homeUrl:'/',
            url: '/vodshow/fyclass--------fypage---.html',
            searchUrl: '/vodsearch/**----------fypage---.html',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 0,//是否启用分类筛选,
            headers: {//网站的请求头,完整支持所有的,常带ua和cookies
                'User-Agent': 'MOBILE_UA',
                // "Cookie": "searchneed=ok"
            },
            class_parse: '.foot_rows li:gt(0):lt(10);span&&Text;a&&href;/(\\d+).html',
            play_parse: true,
            lazy: '',
            limit: 6,
            推荐: '.vodlist_item;a.vodlist_thumb;title&&Text;.lazyload&&data-original;em&&Text;a&&href',
            double: true, // 推荐内容是否双层定位
            一级: '.vodlist_item;a&&title;.lazyload&&data-original;.text_right&&Text;.vodlist_title&&a&&href',
            二级: {
                "title": ".content_thumb&&a.vodlist_thumb&&title",
                "img": ".lazyload&&data-original",
                "desc": ".text_muted:eq(0)&&Text;.module-info-item:eq(1)&&Text;.module-info-item:eq(2)&&Text",
                "content": ".content_desc&&Text",
                "tabs": ".play_source_tab",
                "lists": ".play_list_box:eq(#id) a"
            },
            搜索: 'body .module-item;.module-card-item-title&&Text;.lazyload&&data-original;.module-item-note&&Text;a&&href;.module-info-item-content&&Text',
        }