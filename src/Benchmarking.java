import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento metodosOrdenamiento;
    public Benchmarking(){
        //long inicioMillis = System.currentTimeMillis();
        //long inicioNano = System.nanoTime();

        //System.out.println(inicioMillis + " / " + inicioNano);
        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea = () -> metodosOrdenamiento.burbujaTradicional(arreglo);
        double resultado1 = madirConNanoTime(tarea);
        System.out.println("El timepo con nano time es: "+resultado1);
        double resultado2 = medirConCurrentTime(tarea);
        System.out.println("El tiempo con current time es: "+resultado2);
    }

    public int[] generarArregloAleatorio(int i){
        Random random = new Random();
        int[] arreglo = new int[i];
        for (int j = 0; j < i; j++) {
            arreglo[j] = random.nextInt(10000 );
        }
        return arreglo;
    }

    public double madirConNanoTime(Runnable tarea){
        long incio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - incio) /1_000_000_000.0;

    }

    public double medirConCurrentTime(Runnable tarea){
        long incio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - incio) /1000.0;

    }
}
