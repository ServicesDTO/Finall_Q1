package T2;
import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        
        Toy toy1 = new Toy(1, "конструктор", 2);
        Toy toy2 = new Toy(2, "робот", 2);
        Toy toy3 = new Toy(3, "кукла", 6);

        
        PriorityQueue<Toy> queue = new PriorityQueue<>((t1, t2) -> Integer.compare(t2.getFrequency(), t1.getFrequency()));
        queue.add(toy1);
        queue.add(toy2);
        queue.add(toy3);

        // Генерируем случайные числа для выбора игрушки в соответствии с их частотой выпадения
        Random random = new Random();

        // Вызываем метод Get 10 раз и записываем результаты в файл
        try (FileWriter writer = new FileWriter("results.txt")) {
            for (int i = 0; i < 10; i++) {
                double randomNumber = random.nextDouble();
                Toy chosenToy = chooseToy(queue, randomNumber);
                writer.write(chosenToy.getId() + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static Toy chooseToy(PriorityQueue<Toy> queue, double randomNumber) {
        int cumulativeProbability = 0;
        for (Toy toy : queue) {
            cumulativeProbability += toy.getFrequency();
            if (randomNumber <= (double) cumulativeProbability / 10) {
                return toy;
            }
        }
        return queue.peek();
    }
}