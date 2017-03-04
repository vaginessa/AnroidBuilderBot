package com.android.builder;


public class HttpResponse {
    private String response;

    public HttpResponse() {
    }

    public String getResponse() {

        return response;
    }

    public void setResponse(String response) {
        this.response = response;
    }

    public HttpResponse(String response) {

        this.response = response;
    }
}
