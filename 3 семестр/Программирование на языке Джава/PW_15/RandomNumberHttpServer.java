import java.io.*;
import java.net.*;
import java.util.*;

public class RandomNumberHttpServer
{
    private static final int PORT = 66;
    private static final String STUDENT_NAME = "Враженко Даниил Олегович";
    private static final String STUDENT_ID = "23И0526";
    private static final String URL = "http://localhost:66/random?min=&max=";

    public static void main(String[] args)
    {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("HTTP сервер запущен на порту " + PORT);
            System.out.println("Студент: " + STUDENT_NAME + ", Шифр: " + STUDENT_ID);
            System.out.println("Для проверки работы перейдите по url и добавьте в него min и max значения:\n" + URL);
            while (true)
                try (Socket clientSocket = serverSocket.accept())
                { handleClient(clientSocket); }
        }
        catch (IOException e)
        { System.err.println("Ошибка запуска сервера: " + e.getMessage()); }
    }

    private static void handleClient(Socket clientSocket) throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream());
        String line = in.readLine();
        if (line == null) return;

        String[] requestParts = line.split(" ");
        String method = requestParts[0];
        String path = requestParts[1];

        if (method.equals("GET") && path.startsWith("/random"))
            handleRandomNumberRequest(path, out);
        else
            handleNotFound(out);
        out.flush();
    }

    private static void handleRandomNumberRequest(String path, PrintWriter out)
    {
        try
        {
            Map<String, String> params = parseQueryParams(path);
            int min = Integer.parseInt(params.get("min"));
            int max = Integer.parseInt(params.get("max"));

            if (min > max)
            {
                sendHttpResponse(out, 400, "<html><body><h1>400 Bad Request: min > max</h1></body></html>");
                return;
            }

            int randomNumber = new Random().nextInt(max - min + 1) + min;
            sendHttpResponse(out, 200, "<html><body><h1>Generated Number: " + randomNumber + "</h1></body></html>");
        }
        catch (Exception e)
        { sendHttpResponse(out, 400, "<html><body><h1>400 Bad Request: Invalid parameters</h1></body></html>"); }
    }

    private static Map<String, String> parseQueryParams(String path)
    {
        Map<String, String> params = new HashMap<>();
        String[] parts = path.split("\\?");
        if (parts.length > 1)
        {
            String[] queryParams = parts[1].split("&");
            for (String param : queryParams)
            {
                String[] keyValue = param.split("=");
                if (keyValue.length == 2)
                    params.put(keyValue[0], keyValue[1]);
            }
        }
        return params;
    }

    private static void handleNotFound(PrintWriter out)
    { sendHttpResponse(out, 404, "<html><body><h1>404 Not Found</h1></body></html>"); }

    private static void sendHttpResponse(PrintWriter out, int statusCode, String body)
    {
        out.println("HTTP/1.1 " + statusCode + " OK");
        out.println("Content-Type: text/html");
        out.println("Content-Length: " + body.length());
        out.println();
        out.println(body);
    }
}