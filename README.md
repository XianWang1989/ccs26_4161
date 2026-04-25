# When Tailor-made Goes Astray: Analyzing Security Risks and Misuses in LLM Customization

This repo contains the sampling data we utilized in our paper ‘’**When Tailor-made Goes Astray: Analyzing Security Risks and Misuses in LLM Customization**‘’. We conduct an empirical study to analyze and measure vulnerabilities and misuses in custom GPTs, on three security problems including malicious URLs, code vulnerabilities, and jailbreak attacks.

The repo contains three folders, including **Malicious_URLs**, **Code_Vulnerabilities** and **Jailbreak_Attacks**. **Code_Vulnerabilities** includes two subfolders, **ChatGPT** and **CustomGPT**. **Malicious_URLs** and **Jailbreak_Attacks** includes three subfolders, **ChatGPT** **CustomGPT_General** and **CustomGPT_ScamRelevant**.

## Data Structure
<pre>
├── README.md
├── Malicious_URLs/
│      ├── ChatGPT/
│      │      └── chatgpt_responses.txt
│      └── CustomGPT_General/
│      |      ├── custom_gpt_general_0001.txt
│      |      └── ...
│      └── CustomGPT_ScamRelevant/
│             ├── custom_gpt_scamrelevent_0001.txt
│             └── ...
├── Code_Vulnerabilities/
│      ├── ChatGPT/
│      │      ├── response910-1.py
│      │      └── ...
│      └── CustomGPT/
│             ├── custom_gpt_0001/
│             │       ├── response910-1.py
│             │       └── ...
│             ├── ...
│             └── custom_gpt_0150/
│                     ├── response910-1.py
│                     └── ...
└── Jailbreak_Attacks/
       ├── ChatGPT/
       |      ├── response1-1.txt
       │      └── ...
       └── CustomGPT_General/
       |      ├── custom_gpt_general_0001/
       │      │       ├── response1-1.txt
       │      │       └── ...
       │      └── ...
       └── CustomGPT_ScamRelevant/
              ├── custom_gpt_scamrelevent_0001/
              │       ├── response1-1.txt
              │       └── ...
              └── ...
</pre>

## Malicious_URL

Malicious_URL includes CustomGPT_General, CustomGPT_ScamRelevant and ChatGPT. The CustomGPT_General subfolder includes 900 text files, corresponding to the 900 general custom GPTs we utilized in the Malicious URL experiment. The name of text files is *custom_gpt_general_{index}.txt*.The CustomGPT_ScamRelevant subfolder includes 750 text files, corresponding to the 750 scam relevant custom GPTs we utilized in the Malicious URL experiment. The name of text files is *custom_gpt_scamrelevent_{index}.txt*. The ChatGPT subfolder includes *chatgpt_responses.txt* .

### Code_Vulnerability

Code_Vulnerability includes CustomGPT and ChatGPT. The CustomGPT subfolder includes 150 subfolders, corresponding to the 150 Programming custom GPTs we utilized in the Code Vulnerability experiment. The name of the subfolders is *custom_gpt_{index}*. The ChatGPT includes the response code files of ChatGPT.

In each custom_gpt_{index} subfolder, the response code files are in the folder. The name of the code files is *response{question_index}-{response_index}.py*.

### Jailbreak_Attacks

Jailbreak_Attacks includes CustomGPT_General, CustomGPT_ScamRelevant and ChatGPT. The CustomGPT_General subfolder includes 900 sub folders, corresponding to the 900 general custom GPTs we utilized in the Jailbreak Attacks experiment.  The name of the sub folders is *custom_gpt_general_{index}*. The CustomGPT_ScamRelevant subfolder includes 740 sub folders, corresponding to the 740 scam relevant custom GPTs we utilized in the Jailbreak Attacks experiment (10 scam relevant custom GPTs inaccessible in Jailbreak Attacks experiment).  The name of the sub folders is *custom_gpt_scamrelevent_{index}*. The ChatGPT subfolder includes the response of text files of ChatGPT.

In each *custom_gpt_general_{index}* and *custom_gpt_scamrelevent_{index}* subfolder, 40 text files are included, corresponding to the 5 prompts * 8 scenarios we tested in the experiments. The name of the text files is *response{prompt_index}-{scenario_index}.txt*.
