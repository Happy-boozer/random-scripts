import java.io.File;
import java.util.*;


public class dire {
    public static boolean dir_year(int year, String file_way, String filname) {
        String photo_year = String.valueOf(year).substring(1);
        File papka = new File("C:\\Users\\Alexandr\\Desktop\\photo");
        File FILE_TO_MOVE = new File(file_way);
        boolean result = false;
        for(File item : papka.listFiles()){
            if(photo_year.equals(item.getName())){
                File TARGET_FILE = new File("C:\\Users\\Alexandr\\Desktop\\photo\\"+item.getName() + "\\"+filname);
                System.out.println("filname");
                result = FILE_TO_MOVE.renameTo(TARGET_FILE);

            }
            else {
                File podpapka = new File("C:\\Users\\Alexandr\\Desktop\\photo\\"+photo_year);
                if (podpapka.mkdir()){
                    File TARGET_FILE = new File("C:\\Users\\Alexandr\\Desktop\\photo\\"+photo_year+"\\"+filname);
                    result = FILE_TO_MOVE.renameTo(TARGET_FILE);
                }
            }
        }
        return result;
    }
}
