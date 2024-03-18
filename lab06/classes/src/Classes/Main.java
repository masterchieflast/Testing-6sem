package Classes;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        //variant я решил взять по жруналу 3 варик
        ArrayList<Patien> Patiens = new ArrayList<>();

        // Adding some sample Patiens
        Patiens.add(new Patien(1, "Smith", "John", "Doe", "123 Main St", "123-456-7890", 1001, "Fever"));
        Patiens.add(new Patien(2, "Johnson", "Jane", "Doe", "456 Elm St", "234-567-8901", 1002, "Headache"));
        Patiens.add(new Patien(3, "Williams", "David", "Smith", "789 Oak St", "345-678-9012", 1003, "Broken Leg"));
        Patiens.add(new Patien(4, "Brown", "Emily", "Johnson", "101 Pine St", "456-789-0123", 1004, "Fever"));
        Patiens.add(new Patien(5, "Jones", "Michael", "Williams", "202 Cedar St", "567-890-1234", 1005, "Headache"));

        // Searching for Patiens with a specific diagnosis
        String searchDiagnosis = "Fever";
        System.out.println("Patiens with diagnosis '" + searchDiagnosis + "':");
        for (Patien Patien : Patiens) {
            if (Patien.getDiagnosis().equalsIgnoreCase(searchDiagnosis)) {
                System.out.println(Patien);
            }
        }

        // Searching for Patiens with medical card number in a specified range
        int startMedicalCard = 1002;
        int endMedicalCard = 1004;
        System.out.println("\nPatiens with medical card number between " + startMedicalCard + " and " + endMedicalCard + ":");
        for (Patien Patien : Patiens) {
            int medicalCardNumber = Patien.getMedicalCardNumber();
            if (medicalCardNumber >= startMedicalCard && medicalCardNumber <= endMedicalCard) {
                System.out.println(Patien);
            }
        }

    }
}