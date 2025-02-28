/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.packg.inicie;

import com.squareup.okhttp.Response;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 *
 * @author brawl
 */
public class PeruDni {
    
    private static final String URL = "http://localhost:9095/dni/pe/";
    
    public static void send_dni(String dni){
        try{
            if (dni.length() == 8){
                Response respons = JavaRq.get_rsp(URL + dni);
                if (respons.code() == 200){
                    String json = respons.body().string();
                    Thread.sleep(10000);
                    json_parsing(json);
                }
            }else{
                System.out.print("[!] DNI INVALIDO");
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }
    
    private static void json_parsing(String recibed_json){
        JSONObject jsonObject = new JSONObject(recibed_json);
        if ("sin resultados".equals(jsonObject.getString("found"))){
            System.out.println("[!] Sin resultados");
        }else{
            System.out.print(String.format("Nombre: %s\nApellido M: %s\nApellido P: %s\nRuc: %s\nDigito: %s", 
        jsonObject.getString("nombre"), jsonObject.getString("apellidoM"),jsonObject.getString("apellidoP"), jsonObject.getString("ruc"),jsonObject.getString("digito")));
        }
        
    }
}
