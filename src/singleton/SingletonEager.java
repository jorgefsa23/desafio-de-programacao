package singleton;


/**
 * Singleton apressado
 * @author : jorgefsa23
 */
public class SingletonEager {

    private static SingletonEager instancia = new SingletonEager();

    public SingletonEager() {
        super();
    }

    public static SingletonEager getInstance(){
        return instancia;

    }
}
