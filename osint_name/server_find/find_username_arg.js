const puppeteer = require('puppeteer');
const { text } = require('stream/consumers');
const { array } = require('yargs');

module.exports = {find_user_yt, find_username_fb };

const browser_find = puppeteer.launch({
    headless: "new"
});

async function find_user_yt(user_yt){
    const page_yt = await(await browser_find).newPage();
    await page_yt.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59');
    await page_yt.goto(`https://www.youtube.com/@${user_yt}/about`);
    await new Promise(time_session => setTimeout(time_session, 1000));
    const find_sscr = await page_yt.$('yt-formatted-string#subscriber-count');
    const text_cn = await page_yt.evaluate(elementC => elementC.textContent, find_sscr);
    const find_videos = await page_yt.$('yt-formatted-string#videos-count');
    const text_vd = await page_yt.evaluate(textV => textV.textContent, find_videos);
    const find_ubi = await page_yt.$x('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[2]/td[2]/yt-formatted-string');
    const text_ubi = await page_yt.evaluate(element_ubi => element_ubi.textContent, find_ubi[0])
    const find_st = await page_yt.$x('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[2]/yt-formatted-string[2]/span[2]');
    const text_st = await page_yt.evaluate(element_st => element_st.textContent, find_st[0]);
    const find_sub = await page_yt.$x('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[2]/yt-formatted-string[3]');
    const text_sub = await page_yt.evaluate(element_sub => element_sub.textContent, find_sub[0]);
    const links_profile = await page_yt.evaluate(() => {
        const link_ur = document.querySelector('div#links-container');
        if (link_ur){
            const sett_link = link_ur.querySelectorAll('a');
            return Array.from(sett_link, final_link => final_link.href);
        }
        return []
    
    });
    links_profile.forEach(link => {
        return link
    });
    sett_json = {
        suscriptores: text_cn,
        videos: text_vd,
        ubicacion: text_ubi,
        fecha: text_st,
        subs: text_sub,
        links: links_profile
    }
    return sett_json;
    
}

async function find_username_fb(username_fb){
    const page_facebook = await(await browser_find).newPage();
    await page_facebook.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59');
    await page_facebook.goto(`https://www.facebook.com/${username_fb}/about`)
    await new Promise(time_session_fb => setTimeout(time_session_fb, 1000));
    const show_vn_fb = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div');
    await page_facebook.waitForSelector('div.x78zum5');
    if (show_vn_fb){
        await show_vn_fb[0].click();
        await new Promise(time_session_fb => setTimeout(time_session_fb, 1000));
        const find_link = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li/div/div/div[1]');
        const text_sub = await page_facebook.evaluate(element_link => element_link.textContent, find_link[0]);
        const find_follow = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]');
        const text_follow = await page_facebook.evaluate(element_follow => element_follow.textContent, find_follow[0])
        const find_followr = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[1]');
        const text_followr = await page_facebook.evaluate(element_followr => element_followr.textContent, find_followr[0]);
        try{
            const show_find_fb = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/a');
            if (show_find_fb){
                await show_find_fb[0].click()
                await new Promise(time_session_fb => setTimeout(time_session_fb, 1000));
                const find_id = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/span');
                const text_id = await page_facebook.evaluate(element_id => element_id.textContent, find_id[0]);
                const find_fecha = await page_facebook.$x('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/span');
                const text_fecha = await page_facebook.evaluate(element_fecha => element_fecha.textContent, find_fecha[0]);
                json_profile = {
                    link: text_sub,
                    seguidos: text_follow,
                    seguidores: text_followr,
                    id: text_id,
                    fecha_creacion: text_fecha
                }
                return json_profile;
            }
        }catch{
            return {"errorClick": "click incompletado"};
        }
    }else{
        return {"errorClick": "error inesperado"};
    }
}


