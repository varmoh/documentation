```mermaid
flowchart TD
    Frontend[Frontend] -->|Query| Ruuter(Ruuter - DSL Orchestrator)
    Ruuter -->|Final Response| Frontend

    Ruuter <--> TIM[TIM - Session Cookies]
    Ruuter <--> DataMapper[DataMapper - Handlebars Templates]
    Ruuter <--> ReSQL[ReSQL - PostgreSQL Connector]
    ReSQL <--> PostgreSQL[(PostgreSQL Database)]
```

## Example:

### **Chat Request Flow - init.yml**

### 1. Receive Request
- Endpoint accepts JSON (`message` + `user/device` info).

### 2. Extract Values
- Pull key fields from the request:
  - message content  
  - holidays  
  - device info  

### 3. Check Cookie (Session)
- **If no cookie** → generate new chat UUID.  
- **If cookie exists** → validate it with TIM and extract user info.  

### 4. Generate UUIDs (via Resql and PostgresSQL)
- Always generate:
  - Chat ID  
  - Message ID  

### 5. Configure Session
- Ask **ReSQL** for session length.  
- Use **TIM** to generate a **JWT cookie** with that chat ID.  

### 6. Send Greetings
- Trigger greeting message through a **Ruuter** public endpoint.  

### 7. Store Chat + Message in PostgresSQL (via ReSQL)
- Insert the user’s first message.  
- Create a new chat record (**status: OPEN**).  

### 8. Forward to Bot
- Send the message + holiday data to the bot.  
- **If bot fails** → return `"Bot error"` with status **420**.  

### 9. Fetch Chat & Notify
- Get chat details from **PostgresSQL** using **ReSQL**.  
- Send notifications (chat + message).

### 10. Return Response
- Reply with the chat object.  
- Attach **Set-Cookie** header for the new/validated session. 

```mermaid
flowchart TD
    A[Receive request<br/>JSON with message + device info] --> B["Extract values<br/>(message, holidays, device info)"]
    B --> C{Check cookie?}

    C -->|No cookie| D["Generate new chat UUID<br/>(via PostgresSQL)"]
    C -->|Cookie exists| E[Validate cookie with TIM<br/>Extract user info]

    D --> F["Generate UUIDs<br/>(chatId + messageId)"]
    E --> F
    
    subgraph P[⟶ Parallel actions]
        F --> G[Configure session<br/>ReSQL: get session length]
        F --> H[TIM: generate JWT cookie]
        F --> I[Send greeting<br/>via Ruuter public endpoint]
        F --> J[Store chat + message<br/>in PostgreSQL]
        F --> K[Forward message to bot<br/>via Ruuter internal endpoint]
    end

    K --> L{Bot error?}
    L -->|Yes| M[Return 420 Bot error]
    L -->|No| N[Fetch chat from PostgresSQL using Resql<br/>+ send notifications]

    N --> O[Return response<br/>Chat object + Set-Cookie]
```

 
