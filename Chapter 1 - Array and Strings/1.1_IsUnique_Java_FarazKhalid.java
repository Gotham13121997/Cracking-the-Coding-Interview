public class DuplicateChar{

 
	public static void main(String []args){

         boolean result = false;
        
	String line = "ABCDEFghuioP";
        
        
	line = line.toLowerCase();
        
       
	for (int i=0; i < line.length(); i++) {
     
	       for (int j=0; j < line.length(); j++) {
          
		      if (j == i) 
			{
                 
   
                	}
                

			else {
 
	                   if (line.charAt(i) == line.charAt(j)) 
				{
       
		                 result = true;
                       
				 break;
                
			    	}
      
		          }
            
			}
        
		}
        
      
	  System.out.println("Duplicate Character in String: " + result);
   
	  }

}