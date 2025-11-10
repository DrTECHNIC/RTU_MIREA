import java.util.concurrent.ConcurrentHashMap;

public class AppSettings
{
    private static volatile AppSettings instance;
    private ConcurrentHashMap<String, String> settings;

    private AppSettings()
    { settings = new ConcurrentHashMap<>(); }

    public static AppSettings getInstance()
    {
        if (instance == null) synchronized (AppSettings.class)
            { if (instance == null) instance = new AppSettings(); }
        return instance;
    }

    public void setSetting(String key, String value)
    { settings.put(key, value); }

    public String getSetting(String key)
    { return settings.get(key); }
}

