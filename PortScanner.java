import java.net.*;
import java.io.*;
import java.util.*;
import java.text.SimpleDateFormat;

public class PortScanner {

    public static void main(String[] args) {
        // Check if there is a target host provided as an argument
        if (args.length != 1) {
            System.out.println("Usage: java PortScanner <hostname>");
            return;
        }

        String target = args[0];
        
        // Display banner
        System.out.println("\nPORT SCANNER\n");
        System.out.println("-".repeat(50));

        // Print the scanning details
        System.out.println("Scanning Target: " + target);
        System.out.println("Scanning started at: " + getCurrentTime());
        System.out.println("-".repeat(50));

        // Start scanning ports
        try {
            InetAddress ip = InetAddress.getByName(target);

            // Scan ports from 1 to 65535
            for (int port = 1; port <= 65535; port++) {
                try (Socket socket = new Socket()) {
                    socket.connect(new InetSocketAddress(ip, port), 1000); // Timeout in 1000 ms (1 second)
                    System.out.println("Port " + port + " is open");
                } catch (IOException e) {
                    // Skip closed ports or any connection errors
                }
            }
        } catch (UnknownHostException e) {
            System.out.println("\nHostname Could Not Be Resolved!!!!");
        } catch (SecurityException e) {
            System.out.println("\nServer not responding or permission issues!");
        }
    }

    // Utility method to get current time in a formatted way
    private static String getCurrentTime() {
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Date date = new Date();
        return formatter.format(date);
    }
}