package com.android.builder;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller(value = "/")
public class MainController {
    @GetMapping
    ResponseEntity<
}
