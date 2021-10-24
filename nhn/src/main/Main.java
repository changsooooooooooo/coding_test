package main;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
	    List<Integer> x = new ArrayList<>();
        x.add(3);
        x.add(1);
        x.add(5);
        List<Integer> temp = x.stream()
                .sorted(Comparator.comparing(v->-v))
                .collect(Collectors.toList());

        for(Integer i : temp){
            System.out.println(i);
        }
    }
}
