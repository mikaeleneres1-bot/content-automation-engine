from idea_engine import get_idea

def generate_script():

    topic = get_idea()

    script = f"""
Hoje vamos falar sobre {topic}.

Existem fatos incríveis que poucas pessoas conhecem.

Se você gosta desse tipo de conteúdo,
siga para mais curiosidades.
"""

    return script
