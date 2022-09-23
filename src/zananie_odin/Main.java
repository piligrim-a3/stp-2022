package zananie_odin;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> logs = new HashMap<>();
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader("access.log"));
            String line;
            String ip;
            int bytes;
            while ((line = bufferedReader.readLine()) != null) {
                //если встретится какое либо количество пробелов, то они будут разделителями
                ip = line.split(" +")[2]; //Третий элемент ip-адрес
                bytes = Integer.parseInt(line.split(" +")[4]); //пятый элемент это колво байт
                logs.put(ip, bytes);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(logs);
    }
}
