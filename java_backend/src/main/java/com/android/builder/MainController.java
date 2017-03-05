package com.android.builder;

import org.springframework.core.io.FileSystemResource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


@Service
@Controller(value = "/repo")
public class MainController {

    @PostMapping
    ResponseEntity<?> getApkRequest(@RequestParam("url") String url) {
        System.out.println("url is" + url);
        FileSystemResource apk;
        try {
            System.out.println("script runned");
            int i = runScript(url);

            System.out.println("exit code is");
            if (i != 0) {
                throw new IOException("retunr code non-zero");
            }

            apk = findApk(url);
            if (apk == null) {
                throw new IOException("wasn't founded");
            }

        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>(new HttpResponse("error"), HttpStatus.FORBIDDEN);
        }

        return new ResponseEntity<>(apk, HttpStatus.OK);
    }

    @GetMapping
    ResponseEntity<?> getpic() {
        return new ResponseEntity<Object>(new FileSystemResource("WDF_1039101.jpg"), HttpStatus.OK);
    }

    private int runScript(String repoName) throws IOException, InterruptedException {
        Process start = new ProcessBuilder("./build_apk.sh", repoName).start();
        return start.waitFor();
    }

    private FileSystemResource findApk(String apkRepo) throws IOException {
        Pattern c = Pattern.compile(".+/[a-zA-Z]+$");
        Matcher matcher = c.matcher(apkRepo);
        String group = matcher.group();
        File f = new File(group);

        if (!f.exists()) {
            throw new IOException();
        }
        String absolutePath = f.getAbsolutePath();
        return getApkInPath(absolutePath);
    }

    private FileSystemResource getApkInPath(String p) throws IOException {
        Path path = Paths.get(p);
        Optional<Path> first = Files.walk(path)
                .filter(path1 -> {
                    Pattern c = Pattern.compile(".+\\.apk$");
                    Matcher matcher = c.matcher(path1.getFileName().toString());
                    return matcher.matches();
                }).findFirst();
        return first.map(path1 -> new FileSystemResource(path1.toAbsolutePath().toString())).orElse(null);
    }


}


