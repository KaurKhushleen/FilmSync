mkdir -p ~/.streamlit/

echo = "\
[server]\n\n
port = $PORT\n\
enableCORS = flase\n\
headless = true\n\
\n\
" > ~/.stramlit/config.toml