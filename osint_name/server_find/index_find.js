const express = require('express');
const {find_user_yt} = require('./find_username_arg');
const {find_username_fb} = require('./find_username_arg');

const app_user = express();
app_user.set("port", 9094);
app_user.use(express.json());

app_user.get("/find/user/yt/:user", async (req, res) => {
    const find_yt = await find_user_yt(req.params.user);
    return res.send(find_yt);
});

app_user.get("/find/user/facebook/:usuario", async (req, res) => {
    const find_fb = await find_username_fb(req.params.usuario);
    return res.send(find_fb);
})
app_user.listen(app_user.get("port"), () => {
    console.log(`Servidor Express en el puerto ${app_user.get("port")}`);
});