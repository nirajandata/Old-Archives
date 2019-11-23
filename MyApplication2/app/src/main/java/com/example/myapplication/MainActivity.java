package com.example.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.github.barteksc.pdfviewer.PDFView;
public class MainActivity extends AppCompatActivity {
    PDFView app;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        app=(PDFView)findViewById(R.id.app);
        app.fromAsset("Download Curriculum of Ten Plus Two in Computer Engineering.pdf").load();
    }
}
