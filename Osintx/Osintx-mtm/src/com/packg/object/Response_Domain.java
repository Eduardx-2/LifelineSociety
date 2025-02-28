/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.packg.object;

/**
 *
 * @author Eduardx
 */
public class Response_Domain {

    private String email;
    private String domain;
    private String twitter;
    private String company;
    private Integer phone_number;

    public Response_Domain(String email, String domain, String twitter, String company, Integer phone_number) {
        this.email = email;
        this.domain = domain;
        this.twitter = twitter;
        this.company = company;
        this.phone_number = phone_number;
    }
   
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public String getTwitter() {
        return twitter;
    }

    public void setTwitter(String twitter) {
        this.twitter = twitter;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public Integer getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(Integer phone_number) {
        this.phone_number = phone_number;
    }
    
  
}
