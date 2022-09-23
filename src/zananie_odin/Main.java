package zananie_odin;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

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
                if(logs.containsKey(ip))
                    //если проверяемый ip-адрес уцже был добавлен в нашу Map,
                    //то мы поместим туда текущее значение увеличенное на уже существующее
                    logs.put(ip, bytes + logs.get(ip));
                else
                    //а если ip-адреса не было, то мы просто поместим туда новый ip-адрес и соответствующее ему колво байт
                    logs.put(ip, bytes);
            }
            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


        //создадим новую коллекцию Map, используя существующую, отсортировав и ограничив количество вхождений до 10
        Map<String,Integer> sortedIp =
                logs.entrySet().stream()
                        .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                        .limit(10)
                        .collect(Collectors.toMap(
                                Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));
        new File("out.txt");
        try {
            FileWriter writer = new FileWriter("out.txt");
            for (Map.Entry<String, Integer> e: sortedIp.entrySet()) {
                writer.write("ip-адрес: " + e.getKey() + " байты: " + e.getValue() + "\n");
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
