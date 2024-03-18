package stringss;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String filename = "D:\\study\\sem6\\Testing\\lab06\\classes\\src\\stringss\\input.txt"; // Путь к вашему файлу с текстом
        String text = readFile(filename);

        // 1. Найти наибольшее количество предложений текста, в которых есть одинаковые слова.
        int maxSentencesWithSameWords = findMaxSentencesWithSameWords(text);
        System.out.println("1. Наибольшее количество предложений с одинаковыми словами: " + maxSentencesWithSameWords);

        // 2. Вывести все предложения в порядке возрастания количества слов в каждом из них.
        List<String> sortedSentences = sortSentencesByWordCount(text);
        System.out.println("\n2. Предложения в порядке возрастания количества слов в них:");
        for (String sentence : sortedSentences) {
            System.out.println(sentence);
        }

        // 3. Найти слово в первом предложении, которого нет ни в одном из остальных предложений.
        String uniqueWord = findUniqueWordInFirstSentence(text);
        System.out.println("\n3. Слово в первом предложении, отсутствующее в остальных: " + uniqueWord);


        // 5. В каждом предложении текста поменять местами первое слово с последним.
        String swappedSentences = swapFirstAndLastWords(text);
        System.out.println("\n5. Текст с поменяными местами первым и последним словом в каждом предложении:");
        System.out.println(swappedSentences);


        // 6. Напечатать слова текста в алфавитном порядке по первой букве.
        //    Слова, начинающиеся с новой буквы, печатать с красной строки.
        System.out.println("\n6. Напечатать слова текста в алфавитном порядке по первой букве. Слова, начинающиеся с новой буквы, печатать с красной строки.\n");

        printWordsInAlphabeticalOrder(text);
    }

    private static String readFile(String filename) {
        StringBuilder text = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                text.append(line).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return text.toString();
    }

    private static int findMaxSentencesWithSameWords(String text) {
        String[] sentences = text.split("[.!?]");
        int maxCount = 0;
        for (String sentence : sentences) {
            String[] words = sentence.trim().split("\\s+");
            Set<String> uniqueWords = new HashSet<>(Arrays.asList(words));
            maxCount = Math.max(maxCount, words.length == uniqueWords.size() ? 1 : 0);
        }
        return maxCount;
    }

    private static List<String> sortSentencesByWordCount(String text) {
        List<String> sentences = Arrays.asList(text.split("[.!?]"));
        sentences.sort(Comparator.comparingInt(s -> s.trim().split("\\s+").length));
        return sentences;
    }

    private static String findUniqueWordInFirstSentence(String text) {
        String[] sentences = text.split("[.!?]");
        String[] firstWords = sentences[0].trim().split("\\s+");
        Set<String> uniqueWords = new HashSet<>(Arrays.asList(firstWords));
        for (int i = 1; i < sentences.length; i++) {
            String[] words = sentences[i].trim().split("\\s+");
            uniqueWords.removeAll(Arrays.asList(words));
        }
        return uniqueWords.isEmpty() ? "Отсутствуют" : uniqueWords.iterator().next();
    }

    private static Set<String> findUniqueWordsOfLengthInQuestions(String text, int length) {
        Set<String> uniqueWords = new HashSet<>();
        String[] sentences = text.split("[.!?]");
        for (String sentence : sentences) {
            if (sentence.trim().endsWith("?")) {
                String[] words = sentence.trim().split("\\s+");
                for (String word : words) {
                    // Удаление знаков препинания из слова
                    word = word.replaceAll("[^a-zA-Zа-яА-Я]", "");
                    if (word.length() == length) {
                        uniqueWords.add(word);
                    }
                }
            }
        }
        return uniqueWords;
    }

    private static String swapFirstAndLastWords(String text) {
        StringBuilder result = new StringBuilder();
        String[] sentences = text.split("[.!?]");
        for (String sentence : sentences) {
            String[] words = sentence.trim().split("\\s+");
            if (words.length > 1) {
                String temp = words[0];
                words[0] = words[words.length - 1];
                words[words.length - 1] = temp;
            }
            for (String word : words) {
                result.append(word).append(" ");
            }
            result.append(sentence.trim().endsWith("?") ? "?" : ".");
        }
        return result.toString();
    }
    private static void printWordsInAlphabeticalOrder(String text) {
        String[] words = text.split("\\s+");
        Arrays.sort(words);

        char currentChar = ' ';
        for (String word : words) {
            char firstChar = Character.toLowerCase(word.charAt(0));
            if (firstChar != currentChar) {
                System.out.println();
                currentChar = firstChar;
            }
            System.out.print(word + " ");
        }
    }
}
