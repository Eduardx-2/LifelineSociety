const puppeteer = require('puppeteer');

let showMssg = "❌ No se encontraron datos para el DNI que ingresaste.";

const browser_data = puppeteer.launch({
    headless: "new"
});


async function search_name_dni(data_name){
    const page_browser = await(await browser_data).newPage();
    await page_browser.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59');
    await page_browser.goto('https://eldni.com/pe/buscar-por-nombres');

    await new Promise(resulSet => setTimeout(resulSet, 1000));
    if (data_name.split("|").length == 3){
        await page_browser.type('#nombres', data_name.split("|")[0]);
        await page_browser.type('#apellido_p', data_name.split("|")[1]);
        await page_browser.type('#apellido_m', data_name.split("|")[2]);
    }else {
        return {'person': 'Invalid'}
     
    }
    await new Promise(resulSet => setTimeout(resulSet, 1000));
    await page_browser.click('#btn-buscar-por-nombres');
    await new Promise(resulSet => setTimeout(resulSet, 4000));
    await page_browser.waitForSelector('h4.text-center mark');
    await page_browser.waitForSelector('.table.table-striped.table-scroll');
    const tex_counter = await page_browser.$eval('h4.text-center mark', element_count => element_count.textContent);
    
    if (tex_counter > 0){
        const data = await page_browser.evaluate(() => {
            const rows = Array.from(document.querySelectorAll('.table.table-striped.table-scroll tbody tr'));
        
            return rows.map(row => {
                const columns = Array.from(row.querySelectorAll('th, td'));
                const filtered_anuncio = columns.filter(column => !column.textContent.includes('(adsbygoogle = window.adsbygoogle || []).push({});'));
                return filtered_anuncio.map(column => column.textContent.trim());
            });
        });
    
        const obj_person = data.map(elemento => {
            return {
                dni: elemento[0] || '',
                nombre: elemento[1] || '',
                apellido_p: elemento[2] || '',
                apellido_m: elemento[3] || ''
            };
        });

        await new Promise(resulSet => setTimeout(resulSet, 1000));
       
        return obj_person;
    }else{
        return [{'error': 'La busqueda genero 0 resultados'}];
    
    }
    
}

async function search_dni(dni){
    const page_ = await (await browser_data).newPage();
    await page_.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59')
    await page_.goto('https://eldni.com/pe/buscar-datos-por-dni');
    await new Promise(resulSet => setTimeout(resulSet, 1000));
    if (dni.length == 8){
        await page_.type('.form-input', dni)
    }
    await new Promise(resulSet => setTimeout(resulSet, 1000));
    await page_.click('#btn-buscar-datos-por-dni');
    await new Promise(resulSet => setTimeout(resulSet, 3000));
    const evaluate__Error = await page_.evaluate(() => {
        const err0r_ = Array.from(document.querySelectorAll('h3'));
        return err0r_.map(err0 => err0.textContent.trim());
    })
    if (showMssg === evaluate__Error[1]){
        return [{"found": "sin resultados"}];
        
    }else{
        const show_eval = await page_.evaluate(() => {
            const td_el = Array.from(document.querySelectorAll('td'))
            return td_el.map(td => td.textContent.trim());
        })
        const text_json = {
            nombre: show_eval[1],
            apellidoM: show_eval[2],
            apellidoP: show_eval[3],
            digito: show_eval[4],
            ruc: show_eval[5]
        };
        return text_json;
        
    }
    
}

module.exports = {
    search_name_dni,
    search_dni,
};

