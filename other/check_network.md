
# How to Check Your IP and Test Internet Connection on Windows

## Step 1: Open Command Prompt

1. Press the **Windows key** on your keyboard (the key with the Windows logo).  
2. Type `cmd` in the search box.  
3. Click on **Command Prompt** from the list that appears.  

> 💡 *A black window with white text will open. This is called the Command Prompt.*

## Step 2: See Your IP Configuration

1. In the Command Prompt window, type the following command exactly as shown:  

```cmd
ipconfig
```

2. Press **Enter**.  
3. You will see a list of information. Look for the line called **IPv4 Address**—this is your computer’s IP address on your network.

## Step 3: Test Your Internet Connection with Ping

1. Type the following command:  

```cmd
ping 8.8.8.8
```

2. Press **Enter**.  
3. You will see several lines with `Reply from…` and numbers like `time=20ms`.  

>  *This number shows how fast your computer can reach Google’s server. Smaller numbers are faster, bigger numbers are slower.*

## Step 4: Close Command Prompt

When you are done, simply type:  

```cmd
exit
```

and press **Enter**.  
> *The Command Prompt window will close.*
