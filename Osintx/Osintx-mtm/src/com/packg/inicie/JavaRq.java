/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.packg.inicie;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.util.concurrent.TimeUnit;


/**
 *
 * @author brawl
 */
public class JavaRq {
    
    public static Response get_rsp(String url_send) throws IOException{
        Response resp = null;
        OkHttpClient client = new OkHttpClient();
        client.setConnectTimeout(10, java.util.concurrent.TimeUnit.SECONDS);
        client.setReadTimeout(30, java.util.concurrent.TimeUnit.SECONDS);
        Request rq_url = new Request.Builder()
                .url(url_send)
                .build();
        resp = client.newCall(rq_url).execute();
        return resp;
    }
}
