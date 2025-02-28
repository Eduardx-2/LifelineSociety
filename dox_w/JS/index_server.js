const express = require('express');
const { search_name_dni } = require('./find_pe_name');
const { search_dni } = require('./find_pe_name');

const app_ = express();
app_.set("port", 9095);
app_.use(express.json());

app_.get("/nombre/pe/:nm", async (req, res) => {
    const result_json = await search_name_dni(req.params.nm);
    return res.send(result_json);
});

app_.get("/dni/pe/:dni", async (req, res) =>{
    const body_dni = await search_dni(req.params.dni);
    return res.send(body_dni);
})
app_.listen(app_.get("port"), () => {
    console.log(`Servidor Express en el puerto ${app_.get("port")}`);
});
  
 