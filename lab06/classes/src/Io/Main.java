package Io;

import java.io.*;

public class Main {

    public static void main(String[] args) {

        //String path = "D:/Unity";
        String path = "D:\\study\\sem6\\Testing\\lab06\\classes\\src\\Io\\test.txt";
        File file = new File(path);

        if (file.isDirectory()) {
            analyzeAndWriteToFile(file);
        } else {
            analyzeTextFile(file);
        }
    }

    private static void analyzeAndWriteToFile(File directory) {
        try {
            File outputFile = new File("D:\\study\\sem6\\Testing\\lab06\\classes\\src\\Io\\test.txt");
            FileWriter writer = new FileWriter(outputFile);
            writeDirectoryStructure(directory, writer, 0);
            writer.close();
            System.out.println("Directory structure has been written to test.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void writeDirectoryStructure(File directory, FileWriter writer, int depth) throws IOException {
        File[] files = directory.listFiles();
        if (files == null) {
            return;
        }

        String indent = "    ".repeat(depth);
        for (File file : files) {
            if (file.isDirectory()) {
                writer.write(indent + file.getName() + "\n");
                writeDirectoryStructure(file, writer, depth + 1);
            } else {
                writer.write(indent + "|-----" + file.getName() + "\n");
            }
        }
    }
    private static void analyzeTextFile(File file) {
        int folders = 0;
        int filesCount = 0;
        int totalFileNameLength = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    String[] parts = line.trim().split(" ");
                    if (parts.length > 1 && parts[1].length() > 0) {
                        filesCount++;
                        totalFileNameLength += parts[1].length();
                    } else {
                        folders++;
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        double averageFilesPerFolder = (double) filesCount / folders;
        double averageFileNameLength = (double) totalFileNameLength / filesCount;

        System.out.println("Number of folders: " + folders);
        System.out.println("Number of files: " + filesCount);
        System.out.println("Average number of files per folder: " + averageFilesPerFolder);
        System.out.println("Average length of file name: " + averageFileNameLength);
    }
}
