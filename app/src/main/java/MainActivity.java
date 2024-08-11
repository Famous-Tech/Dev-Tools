package com.example.devtools;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button openFileButton = findViewById(R.id.openFileButton);
        Button createFileButton = findViewById(R.id.createFileButton);
        Button manageFoldersButton = findViewById(R.id.manageFoldersButton);
        TextView tutorialText = findViewById(R.id.tutorialText);

        openFileButton.setOnClickListener(v -> {
            // Code pour ouvrir un fichier
        });

        createFileButton.setOnClickListener(v -> {
            // Code pour créer un fichier
        });

        manageFoldersButton.setOnClickListener(v -> {
            // Code pour gérer les dossiers
        });

        tutorialText.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, TutorialActivity.class);
            startActivity(intent);
        });
    }
}
