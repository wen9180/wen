import { Spider } from "../spider.js";
import req from '../../util/req.js';
import CryptoJS from 'crypto-js';

// let siteUrl = 'http://ys.changmengyun.com';

let siteUrl = 'http://ys.changmengyun.com';

class NanguaSpider extends Spider {

    constructor() {
        super();
        this.siteUrl = 'http://ys.changmengyun.com';
    }

    getName() { return "🎃|南瓜影视" }

    getAppName() { return "南瓜影视" }

    getJSName() { return "nangua" }

    async request(reqUrl){
        let res = await req(reqUrl, {
            headers: this.getHeaders(),
            method: 'get',
        });
        let content = res.data;
        return content;
    }
    
    async init(inReq, _outResp) {
        this.siteUrl = inReq.server.config.nangua.url;
        return {};
    }
    
    async home(_inReq, _outResp) {
       
        return JSON.stringify({
            'class': [{'type_id':'1','type_name':'电影'},{'type_id':'2','type_name':'电视剧'},{'type_id':'4','type_name':'动漫'},{'type_id':'3','type_name':'综艺'},{'type_id':'46','type_name':'海外精选'}],
            'filters': {
                "2":[{"key":"class","name":"类型","value":[{"n":"全部","v":"类型"},{"n":"国产剧","v":"国产剧"},{"n":"港台剧","v":"港台剧"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"地区"},{"n":"内地","v":"内地"},{"n":"香港地区","v":"香港地区"},{"n":"台湾地区","v":"台湾地区"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":"年份"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"10年代","v":"10年代"},{"n":"00年代","v":"00年代"},{"n":"90年代","v":"90年代"},{"n":"80年代","v":"80年代"}]},{"key":"by","name":"排序","value":[{"n":"热播榜","v":"热播榜"},{"n":"好评榜","v":"好评榜"},{"n":"新上线","v":"新上线"}]}],
                "1":[{"key":"class","name":"类型","value":[{"n":"全部","v":"类型"},{"n":"动作片","v":"动作片"},{"n":"喜剧片","v":"喜剧片"},{"n":"爱情片","v":"爱情片"},{"n":"科幻片","v":"科幻片"},{"n":"恐怖片","v":"恐怖片"},{"n":"剧情片","v":"剧情片"},{"n":"战争片","v":"战争片"},{"n":"惊悚片","v":"惊悚片"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"地区"},{"n":"华语","v":"华语"},{"n":"香港地区","v":"香港地区"},{"n":"美国","v":"美国"},{"n":"欧洲","v":"欧洲"},{"n":"韩国","v":"韩国"},{"n":"日本","v":"日本"},{"n":"台湾地区","v":"台湾地区"},{"n":"泰国","v":"泰国"},{"n":"台湾地区","v":"台湾地区"},{"n":"印度","v":"印度"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":"年份"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"10年代","v":"10年代"},{"n":"00年代","v":"00年代"},{"n":"90年代","v":"90年代"},{"n":"80年代","v":"80年代"}]},{"key":"by","name":"排序","value":[{"n":"热播榜","v":"热播榜"},{"n":"好评榜","v":"好评榜"},{"n":"新上线","v":"新上线"}]}],
                "4":[{"key":"class","name":"类型","value":[{"n":"全部","v":"类型"},{"n":"国产漫","v":"国产漫"},{"n":"欧美漫","v":"欧美漫"},{"n":"日韩漫","v":"日韩漫"},{"n":"港台漫","v":"港台漫"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"地区"},{"n":"中国大陆","v":"中国大陆"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"欧美","v":"欧美"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":"年份"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"10年代","v":"10年代"},{"n":"00年代","v":"00年代"},{"n":"90年代","v":"90年代"},{"n":"80年代","v":"80年代"}]},{"key":"by","name":"排序","value":[{"n":"热播榜","v":"热播榜"},{"n":"新上线","v":"新上线"}]},{"key":"total","name":"状态","value":[{"n":"全部","v":"状态"},{"n":"连载","v":"连载"},{"n":"完结","v":"完结"}]}],
                "3":[{"key":"class","name":"类型","value":[{"n":"全部","v":"类型"},{"n":"大陆","v":"大陆"},{"n":"港台","v":"港台"},{"n":"日韩","v":"日韩"},{"n":"欧美","v":"欧美"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"地区"},{"n":"内地","v":"内地"},{"n":"港台","v":"港台"},{"n":"日韩","v":"日韩"},{"n":"欧美","v":"欧美"},{"n":"其它","v":"其它"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":"年份"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"10年代","v":"10年代"},{"n":"00年代","v":"00年代"},{"n":"90年代","v":"90年代"},{"n":"80年代","v":"80年代"}]},{"key":"by","name":"排序","value":[{"n":"热播榜","v":"热播榜"},{"n":"新上线","v":"新上线"}]}],
                "46":[{"key":"class","name":"类型","value":[{"n":"全部","v":"类型"},{"n":"日韩剧","v":"日韩剧"},{"n":"欧美剧","v":"欧美剧"},{"n":"海外剧","v":"海外剧"}]},{"key":"area","name":"地区","value":[{"n":"全部","v":"地区"},{"n":"韩国","v":"韩国"},{"n":"美剧","v":"美剧"},{"n":"日本","v":"日本"},{"n":"泰国","v":"泰国"},{"n":"英国","v":"英国"},{"n":"新加坡","v":"新加坡"},{"n":"其他","v":"其他"}]},{"key":"year","name":"年份","value":[{"n":"全部","v":"年份"},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"10年代","v":"10年代"},{"n":"00年代","v":"00年代"},{"n":"90年代","v":"90年代"},{"n":"80年代","v":"80年代"}]},{"key":"by","name":"排序","value":[{"n":"热播榜","v":"热播榜"},{"n":"好评榜","v":"好评榜"},{"n":"新上线","v":"新上线"}]}]
            },
        });
    }
    
    // tid, pg, filter, extend
    async category(inReq, _outResp) {
    
        const tid = inReq.body.id;
        let pg = inReq.body.page;
        const extend = inReq.body.filters;
    
        if(pg <= 0) pg = 1;
        let area = extend['area']?extend['area']:'';
        let year = extend['year']?extend['year']:'';
        let type = extend['class']?extend['class']:'';
        
        let url = this.siteUrl + '/api.php/provide/vod_list?app=ylys&id='+tid+'&area='+ area +'&year='+year+'&type='+type+'&page='+pg+'&imei=c431ea542cee9679';
        // let res = JSON.parse(await request(url));
        
        let res = await this.request(url);
        
        // 换普通处理方法
        let  videos = [];
        for (const vod of res['list']) {
            let a =  {
            vod_id: vod.id,
            vod_name: vod.name,
            vod_pic: vod.img,
            vod_remarks: vod.msg,
            }
            videos.push(a);
         }
    
        return JSON.stringify({
            page: pg,
            limit: res['limit'],
            list: videos,
        });
    }
    
    async detail(inReq, _outResp) {
        const ids = !Array.isArray(inReq.body.id) ? [inReq.body.id] : inReq.body.id;
        const videos = [];
    
        for (const id of ids) {
            // let data = JSON.parse(await request(siteUrl + '/api.php/provide/vod_detail?app=ylys&imei=c431ea542cee9679&id=' + id))['data'];
            let data = (await this.request(this.siteUrl + '/api.php/provide/vod_detail?app=ylys&imei=c431ea542cee9679&id=' + id))['data'];
            let vod = {
                vod_name: data.name,
                vod_pic: data.img,
                type_name: data.type,
                vod_year: data.year,
                vod_remarks: data.msg,
                vod_content: '公众号：【蚂蚁科技杂谈】' + data.info,
            };
            let episodes = data.player_info;
            let playFroms = [];
            let playUrls = [];
            for (let i=0;i<episodes.length;i++) {
                let episode = episodes[i];
                playFroms.push(episode.show);
                let nameUrls = [];
                for (const play of episode.video_info) {
                    nameUrls.push(play.name + '$' + play['url'][0]);
                }
                playUrls.push(nameUrls.join('#'));
            }
            vod.vod_play_from = playFroms.join('$$$');
            vod.vod_play_url = playUrls.join('$$$');
            videos.push(vod);
        }
    
        return {
            list: videos,
        };
    }
    
    async play(inReq, _outResp) {
        const id = inReq.body.id;
        var parse = [];
        try {
            let input = {parse: 0,url: id,};
            if (id.indexOf(',') > 0) {
                    let mjurl = id.split(',')[1]
                    let videoUrl = await this.getvideo(mjurl);
                    input = {
                        jx: 0,
                        url: videoUrl,
                        parse: 0,
                        header: JSON.stringify({
                            'user-agent': 'Lavf/58.12.100'
                        })
                    }
            } else {
                let videoUrl = await this.getvideo(id);
                if (videoUrl.indexOf('jhapi') > 0) {
                    videoUrl = await this.getvideo(videoUrl);
                    input = {
                        jx: 0,
                        url: videoUrl,
                        parse: 0,
                        header: JSON.stringify({
                            'user-agent': 'Lavf/58.12.100'
                        })
                    }
                } else {
                    input = {
                        jx: 0,
                        url: videoUrl,
                        parse: 0
                    }
                }
            }
            return JSON.stringify(input);
        } catch (e) {
            return JSON.stringify({
                parse: 0,
                url: id,
            });
        }
    }
    
    async getvideo(url) {
        // let jData = JSON.parse(await request(url));
        let jData = (await this.request(url));
        if (jData.code == 1) {
            // console.log("play url = " + jData.data.url);
            return jData.data.url
        } else {
            return 'http://43.154.104.152:1234/jhapi/cs.php?url=' + url.split('=')[1]
        }
    }
    
    async search(inReq, _outResp) {
        const pg = inReq.body.page;
        const wd = inReq.body.wd;
        let page = pg || 1;
        if (page == 0) page = 1;
        // let data = JSON.parse(await request(siteUrl + '/api.php/provide/search_result_more?app=ylys&video_name='+wd+'&pageSize=20&tid=0&imei=c431ea542cee9679&page='+page));
        let data = (await this.request(this.siteUrl + '/api.php/provide/search_result_more?app=ylys&video_name='+wd+'&pageSize=20&tid=0&imei=c431ea542cee9679&page='+page));
        // console.log(data);
        let videos = [];
        // for (const vod of data.data) {
        for (const vod of data.data) {
            videos.push({
                vod_id: vod.id,
                vod_name: vod.video_name,
                vod_pic: vod.img,
                vod_remarks: vod.qingxidu,
            });
        }
        return JSON.stringify({
            page: page,
            list: videos,
        });
    }
    
    getHeaders() {
        let t = new Date().getTime().toString();
        return {
            'version_name': '1.0.6',
            'version_code': '6',
            'package_name': 'com.app.nanguatv',
            'sign': CryptoJS.MD5('c431ea542cee9679#uBFszdEM0oL0JRn@' + t).toString().toUpperCase(),
            'imei': 'c431ea542cee9679',
            'timeMillis': t,
            'User-Agent': 'okhttp/4.6.0'
        };
    }
}

let spider = new NanguaSpider()

const routeHandlers = ['init', 'home', 'category', 'detail', 'play', 'search', 'test'];

const routes = {
    meta: {
        key: spider.getJSName(), name: spider.getName(), type: spider.getType(),
    }, 
    api: async (fastify) => {
        for (const handler of routeHandlers) {
            fastify.post(`/${handler}`, async (inReq, _outResp) => {
                return await spider[handler](inReq, _outResp);
            });
        }
        fastify.get('/test', async (inReq, _outResp) => {
            return await spider.test(inReq, _outResp);
        });
    },
};

export default routes;