package Game;

import java.io.IOException;
import java.util.Arrays;
import java.util.Random;
import  java.util.Scanner;

public class DiceGame {

    private int index(int[] array){
        int largest = 0;
        for (int i = 1; i<array.length; i++){
            if( array[i] > array[largest]){
                largest = i;
            }
        }
        return largest;
    }
    public void Game(int num) throws IOException {
        Scanner scanner = new Scanner(System.in);
        String[] names = new String[num];
        int [] numbers = new int[num];
        for (int i = 0; i < num; i++){
            System.out.println("ВВедите имя игрока");
            String name;
            name = scanner.nextLine();
            names[i] = name;
            Random randon = new Random();
            numbers[i] = randon.nextInt(97);
        }
        int index = index(numbers);
        System.out.println(names[index]);
        System.out.println(numbers[index]);
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ведите количество игроков");
        int num = 0;
        num = scanner.nextInt();
        DiceGame game = new DiceGame();
        game.Game(num);
    }
}

