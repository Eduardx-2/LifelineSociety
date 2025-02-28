/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.packg.inicie;


import com.packg.object.Response_Domain;
import com.squareup.okhttp.Response;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import org.json.JSONObject;

/**
 *
 * @author Eduardx
 */
public class Osintx_sr { 
    private static String URL_EMAIL = "https://api.hunter.io/v2/email-finder?";
    private static final Scanner data_entry = new Scanner(System.in);
    private static String TOKEN = null;
    
    public static void osintx_op(){
        String options;
        try{
            String banner = "________                                  ________         .__        __          \n" +
"\\______ \\   ____   _____   ____           \\_____  \\   _____|__| _____/  |____  ___\n" +
" |    |  \\_/ __ \\ /     \\ /  _ \\   ______  /   |   \\ /  ___/  |/    \\   __\\  \\/  /\n" +
" |    `   \\  ___/|  Y Y  (  <_> ) /_____/ /    |    \\\\___ \\|  |   |  \\  |  >    < \n" +
"/_______  /\\___  >__|_|  /\\____/          \\_______  /____  >__|___|  /__| /__/\\_ \\\n" +
"        \\/     \\/      \\/                         \\/     \\/        \\/           \\/";
            String options_d = "\n[+] - Busqueda Email Dominio\n[+] - Busqueda Email\n[+] - Busqueda de nombres(Pe)\n[+] - Consulta dni(Pe)";
            System.out.println(banner);
            System.out.println(options_d);
            Scanner scan_op = new Scanner(System.in);
            System.out.print("[OPTIONS] -> ");
            options = scan_op.nextLine();
            if (null != options.toLowerCase())switch (options.toLowerCase()) {
                case "pe_name" -> menu_name_pe();
                case "find_email" -> menu_find_email();
                case "pe_dni" -> dni_find();
                default -> {
                    System.out.print("[*] Ingresaste un comando equivocado\n");
                }
            }
        }catch(IOException | InterruptedException e){
            System.out.println(e);
        }
    }
    
    private static void menu_name_pe() throws InterruptedException{
        System.out.print("[NAME] -> ");
        String name_sr = data_entry.nextLine();
        PeruName.find_name(name_sr);
    }
    
    private static void menu_find_email() throws IOException{
        System.out.print("[FIND] -> ");
        String entry_dt = data_entry.nextLine();
        String[] final_to_entry = entry_dt.split("\\|");
        if (final_to_entry.length == 3){
            String part = String.format("domain=%s&first_name=%s&last_name=%s&api_key=%s", final_to_entry[0], final_to_entry[1], final_to_entry[2], file_session_token());
            Response response_rq = JavaRq.get_rsp(URL_EMAIL + part);
            if (response_rq.code() == 200){
                String resp_json = response_rq.body().string();
                parse_json(resp_json);
            }
        }else{
            System.out.println("[ERROR] -> fomato example.com|ex|ex1");
        }
    }
    
    private static void parse_json(String find_js0n){
        JSONObject json = new JSONObject(find_js0n);
        JSONObject data = json.getJSONObject("data");
        
        String dmn = data.getString("domain");
        String email = data.getString("email");
        
        System.out.println(String.format("[ENCONTRADO]:\n Dominio: %s\nEmail: %s", dmn,  email));
    }
    
    private static void dni_find(){
        System.out.print("[DNI] -> ");
        String dni = data_entry.nextLine();
        PeruDni.send_dni(dni);
    }
    
    private static String file_session_token(){
        String t0ken = "";
        String dire = System.getProperty("user.home");
        System.out.println(dire);
        try{
            File len_archive = new File(String.format("%s\\Red_LifelineV1.2\\Red_Lifeline\\clave.txt", dire));
            FileReader session_file = new FileReader(len_archive);
            BufferedReader buffer = new BufferedReader(session_file);
            while((t0ken = buffer.readLine()) != null){
                TOKEN = t0ken;
                      
            }
        }catch(IOException e){
            System.out.println(e);
        }
        return TOKEN;
    }
    
}

   