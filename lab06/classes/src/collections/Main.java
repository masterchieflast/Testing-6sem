package collections;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ApplianceManager manager = new ApplianceManager();

        while (true) {
            System.out.println("1. Подключить электроприбор");
            System.out.println("2. Подсчитать потребляемую мощность");
            System.out.println("3. Отсортировать электроприборы по мощности");
            System.out.println("4. Найти электроприбор в заданном диапазоне мощности");
            System.out.println("5. Выход");

            System.out.print("Выберите действие: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addAppliance(manager);
                    break;
                case 2:
                    calculateTotalPower(manager);
                    break;
                case 3:
                    sortAppliancesByPower(manager);
                    break;
                case 4:
                    findApplianceByPowerRange(manager);
                    break;
                case 5:
                    System.out.println("Выход из программы.");
                    return;
                default:
                    System.out.println("Некорректный ввод. Пожалуйста, выберите действие из списка.");
            }
        }
    }

    private static void addAppliance(ApplianceManager manager) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите название электроприбора: ");
        String name = scanner.nextLine();
        System.out.print("Введите мощность электроприбора: ");
        int power = scanner.nextInt();
        scanner.nextLine();
        System.out.println();

        manager.plugIn(new Lamp(name, power));
    }

    private static void calculateTotalPower(ApplianceManager manager) {
        int totalPower = manager.calculateTotalPower();
        System.out.println("Потребляемая мощность: " + totalPower + " Вт");
    }

    private static void sortAppliancesByPower(ApplianceManager manager) {
        manager.sortByPower();
        System.out.println("Электроприборы отсортированы по мощности.");
    }

    private static void findApplianceByPowerRange(ApplianceManager manager) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите минимальную мощность: ");
        int minPower = scanner.nextInt();
        System.out.print("Введите максимальную мощность: ");
        int maxPower = scanner.nextInt();

        ElectricalAppliance appliance = manager.findApplianceByPowerRange(minPower, maxPower);
        if (appliance != null) {
            System.out.println("Найден электроприбор: " + appliance.getName() + " с мощностью " + appliance.getPower() + " Вт");
        } else {
            System.out.println("Нет электроприборов в заданном диапазоне мощности.");
        }
    }
}
