package singleton;


/**
 * Singleton preguiçoso
 * @author : jorgefsa23
 */
public class SingletonLazy {

    private static SingletonLazy instancia;

    public SingletonLazy() {
        super();
    }

    public static SingletonLazy getInstance(){
        if (instancia == null){
            instancia = new SingletonLazy();
        }
        return instancia;

    }
}
