An Introduction to the LangChain Python Library
###############################################
:date: 2023-10-02 15:15
:author: lofipython
:category: coding, programming, python, artificial intelligence, AI
:tags: python large language models, python LLM, langchain python introduction, python LLM orchestration
:slug: an-introduction-to-the-langchain-python-library
:status: published

LangChain is a lauded Python library in the `large language model <https://en.wikipedia.org/wiki/Large_language_model>`__ space. It seems to be riding along on the AI hype train as of late and is getting mentioned everywhere I look. I wrote this post to understand better, what is LangChain? Warning: I learned a lot by researching for this post! Below you'll find basic information about what LangChain is and code examples for a few of its use cases. I connected a few different sources that helped me fill in the gaps in my knowledge. After reading this, you'll have a basic understanding of what this Python module does and some of the diverse ways it can be applied.

A huge bonus of this library is that it has `excellent documentation <https://python.langchain.com/docs/get_started/quickstart>`__. On the front page, they state its main value propositions.

    The main value props of LangChain are:

    Components: abstractions for working with language models, along with a collection of implementations for each  abstraction. Components are modular and easy-to-use, whether you are using the rest of the LangChain framework or not
    
    
    Off-the-shelf chains: a structured assembly of components for accomplishing specific higher-level tasks
    Off-the-shelf chains make it easy to get started. For complex applications, components make it easy to customize existing chains and build new ones.


The Github repo states LangChain is for "Building applications with LLMs through composability". Ok, so what is composability?

    Composability is a system design principle that deals with the inter-relationships of components. A highly composable system provides components that can be selected and assembled in various combinations to satisfy specific user requirements. \- `Wikipedia <https://en.wikipedia.org/wiki/Large_language_model>`__


LangChain is important because it provides the function of "orchestration" in an LLM serving workflow:

    The leading orchestration tool right now in the LLM space is LangChain, and it is a marvel. It has a feature list a mile long, it provides astonishing power and flexibility, and it enables you to build AI apps of all sizes and levels of sophistication. But with that power comes quite a bit of complexity. Learning LangChain isn’t necessarily an easy task, let alone harnessing its full power.
    
    \- Stephen Hood, `So you want to build your own open source chatbot… – Mozilla Hacks <https://hacks.mozilla.org/2023/07/so-you-want-to-build-your-own-open-source-chatbot>`__

Sometimes an orchestration tool is required, but sometimes you can "roll your own" in a sense, as Mozilla did in their post about serving an LLM. When making your own large language model, you'll want to consider how it will be orchestrated. This is the functionality LangChain provides. In more complex LLM flows that involve tasks like writing code and subsequently running it, LangChain is essential.

    Often people hook up LLMs as part of a sequence of operations. LangChain does this. It puts an LLM in series with some other tools. For instance, LLMs can’t do math, they just spout plausible answers. They can write code, because they’ve read so much of it in their training. By themselves, they can’t use it. But configure a LangChain agent with both an LLM and a Python interpreter, and it can answer word problems. First ask the LLM for a plan to solve the problem, given a Python interpreter; then when the LLM returns code, run it; then provide the answer to the LLM so it can structure the final response.
    
    \- Jessica Kerr, `A Developer’s Starting Point for Integrating with LLMs <https://jessitron.com/2023/09/04/a-developers-guide-to-integrating-with-llms>`__

You'll also want to consider if you need to tune your own AI model, but beware that this can cost a lot of money in compute resources consumed. It seems more likely that for the AI-layperson coder, going with an off-the-shelf model via an API or open source code base makes more fiscal sense and is probably easier. However, you may achieve a unique quality of response by tuning your model to your specific use case, or providing examples as tokens for the model to consume before responding.

    Model training needs lots and lots of machines in relatively close proximity to one another. It needs the absolute latest, greatest GPUs.
    
    \- Matthew Prince, James Governor, `Cloudflare as an AI play. An Interview with Matthew Prince <https://redmonk.com/jgovernor/2023/07/17/cloudflare-as-an-ai-play-an-interview-with-ceo-matthew-prince>`__


**An Example LLM Stack With LangChain**

.. image:: {static}/blog/images/MozillaAssistantdiagram.png
  :alt: Overview of an LLM stack from Mozilla

source: `So you want to build your own open source chatbot… – Mozilla Hacks <https://hacks.mozilla.org/2023/07/so-you-want-to-build-your-own-open-source-chatbot>`__

**Installing the Python Libraries with pip**


.. code:: console

   pip install langchain[all]


.. code:: console

   pip install openai


**The Two Types of Language Models**

    There are two types of language models, which in LangChain are called:

    LLMs: this is a language model which takes a string as input and returns a string
    
    ChatModels: this is a language model which takes a list of messages as input and returns a message


**Calling OpenAI Without a Chain from LangChain**


.. code-block:: python
    
    from langchain.llms import OpenAI

    llm = OpenAI(openai_api_key="...")
    text = "What would be a good company name for a company that makes colorful socks?"
    llm.predict(text)
    # >> Feetful of Fun
    chat_model.predict(text)
    # >> Socks O'Color


**Chaining Components with LangChain**

The chains are a Python class, as demonstrated in this psuedo-code from their docs.

    Using an LLM in isolation is fine for simple applications, but more complex applications require chaining LLMs - either with each other or with other components.

    LangChain provides the Chain interface for such "chained" applications. We define a Chain very generically as a sequence of calls to components, which can include other chains. The base interface is simple: 
    
    \- `LangChain Documentation, Chains How-To <https://python.langchain.com/docs/modules/chains/>`__


.. code-block:: python

    class Chain(BaseModel, ABC):
        """Base interface that all chains should implement."""

        memory: BaseMemory
        callbacks: Callbacks

        def __call__(
            self,
            inputs: Any,
            return_only_outputs: bool = False,
            callbacks: Callbacks = None,
        ) -> Dict[str, Any]:
            ...

**Chaining Open AI Components**

.. code-block:: python

    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    # Run the chain only specifying the input variable.
    print(chain.run("colorful socks"))
    # >> Socks O'Color


**Natural Language Queries with LangChain**

These examples are shown in `Analyzing Structured Data <https://python.langchain.com/docs/use_cases/qa_structured/sql/>`__.

.. code-block:: python

    from langchain.utilities import SQLDatabase
    from langchain.llms import OpenAI
    from langchain_experimental.sql import SQLDatabaseChain

    # The documented examples use a Chinook DB.
    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    llm = OpenAI(temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    db_chain.run("How many employees are there?")
    # >>> 'There are 8 employees.'
    
    
**Text to SQL Queries With Ability to Run the Query on the Database**

 .. code-block:: python
 
    from langchain.utilities import SQLDatabase
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import create_sql_query_chain
   
    chain = create_sql_query_chain(ChatOpenAI(temperature=0), db)
    response = chain.invoke({"question":"How many employees are there"})
    print(response)
    # >>> 'There are 8 employees.'


**Use a LangChain Agent to Describe a Database Table**

 .. code-block:: python
 
    from langchain.agents import create_sql_agent
    from langchain.agents.agent_toolkits import SQLDatabaseToolkit
    # from langchain.agents import AgentExecutor
    from langchain.agents.agent_types import AgentType

    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    llm = OpenAI(temperature=0, verbose=True)
    agent_executor = create_sql_agent(
        llm=OpenAI(temperature=0),
        toolkit=SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0)),
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    agent_executor.run("Describe the playlisttrack table")


**Description of Database Table Result**

 .. code-block:: console

    > Entering new AgentExecutor chain...
    Action: sql_db_list_tables
    Action Input: 
    Observation: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
    Thought: The PlaylistTrack table is the most relevant to the question.
    Action: sql_db_schema
    Action Input: PlaylistTrack
    Observation: 
    CREATE TABLE "PlaylistTrack" (
        "PlaylistId" INTEGER NOT NULL, 
        "TrackId" INTEGER NOT NULL, 
        PRIMARY KEY ("PlaylistId", "TrackId"), 
        FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"), 
        FOREIGN KEY("PlaylistId") REFERENCES "Playlist" ("PlaylistId")
    )
    
    /*
    3 rows from PlaylistTrack table:
    PlaylistId  TrackId
    1   3402
    1   3389
    1   3390
    */
    Thought: I now know the final answer
    Final Answer: The PlaylistTrack table contains two columns, PlaylistId and TrackId, which are both integers and form a primary key. It also has two foreign keys, one to the Track table    and one to the Playlist table.
    
    > Finished chain.
    

**Versatile + Flexible for Your LLM Needs**

If you prefer using the Meta's LLaMA model over OpenAI, more power to you. LangChain can do both and many more. At the time of this writing, the following models are documented: Anthropic, Anthropic Functions, Anyscale, Azure, Azure ML Chat Online Interface, Baidu Qianfan, Bedrock Chat, ERNIE-bot Chat, Fireworks, GCP Vertex API, JinaChat, Konko, LiteLLM, Llama API, MiniMax, Ollama, OpenAI, PromptLayer ChatOpenAI and vLLM Chat.

**Wrapping Up With LangChain**

These examples represent a few things you can do with this popular Python library. You're now a step closer to creating your next AI-infused product or service. No one needs to know it's just a wrapper for OpenAI and LangChain! The library's name makes more sense once you understand a bit of its context as orchestrator. It chains together the pieces of your large language model's parts into a shiny, impressive AI solution. 

**Read More:**

`LangChain Documentation, Chains How To <https://python.langchain.com/docs/modules/chains/how_to/>`__

`LangChain Documentation, Deployments <https://python.langchain.com/docs/guides/deployments/>`__

