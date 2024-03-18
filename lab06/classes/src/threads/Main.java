package threads;

import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;

class Tunnel {
    private Semaphore semaphore;

    public Tunnel(int permits) {
        semaphore = new Semaphore(permits);
    }

    public void enter(int trainId) {
        try {
            semaphore.acquire();
            System.out.println("Train " + trainId + " entered the tunnel.");
            Thread.sleep(new Random().nextInt(3000)); // Simulating time spent in the tunnel
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            System.out.println("Train " + trainId + " exited the tunnel.");
            semaphore.release();
        }
    }
}

class Train implements Runnable {
    private int id;
    private Tunnel tunnel;

    public Train(int id, Tunnel tunnel) {
        this.id = id;
        this.tunnel = tunnel;
    }

    @Override
    public void run() {
        tunnel.enter(id);
    }
}

public class Main {
    public static void main(String[] args) {
        Tunnel tunnel = new Tunnel(2); // 2 permits for two-way traffic
        ExecutorService executor = Executors.newCachedThreadPool();

        // Creating and starting trains
        for (int i = 0; i < 10; i++) {
            executor.execute(new Train(i, tunnel));
        }

        executor.shutdown();
    }
}
