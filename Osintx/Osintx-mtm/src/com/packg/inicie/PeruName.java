/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.packg.inicie;

import com.squareup.okhttp.Response;
import java.io.IOException;
import java.util.Arrays;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 *
 * @author brawl
 */
public class PeruName {
    
    private static final String URI = "http://localhost:9095/nombre/pe/";
    
    public static void find_name(String find) throws InterruptedException{
        try{
            String[] show_find = find.split("\\s+");
            if (show_find.length == 3){
                String x0r_name = String.format("%s|%s|%s", show_find[0], show_find[1], show_find[2]);
                Response respons3_p = JavaRq.get_rsp(URI + x0r_name);
                if (respons3_p.code() == 200){
                    String respons = respons3_p.body().string();
                    Thread.sleep(10000);
                    json_parsed(respons);
                }
             }
        }catch(IOException e){
            System.out.println(e);
        }
    }
    
    private static void json_parsed(String json){
        JSONArray json_str = new JSONArray(json);
        for (int i=0; i < json_str.length(); i++){ 
            JSONObject jsonObject = json_str.getJSONObject(i);
            if ("La busqueda genero 0 resultados".equals(jsonObject.getString("error"))){
                System.out.println("[!]- Sin resultados");
            }else{
                System.out.println(String.format("\nDni: %s\nNombre: %s\nApellido M: %s\nApellido P: %s\n--------------------------------", 
                    jsonObject.getString("dni"), jsonObject.getString("nombre"), jsonObject.getString("apellido_m"),jsonObject.getString("apellido_p")));
            } 
        }
 
    }
}
