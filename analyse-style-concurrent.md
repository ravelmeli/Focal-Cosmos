# Analyse du Short concurrent (« Starlink / Netflix en pleine mer »)

Source : mp4 1080x1920, 60 fps, 80,8 s, AAC mono 44,1 kHz, ~26 Mo. Langue : anglais.

## Format
- Vertical 9:16, 1080x1920, 60 fps.
- Durée 80 s : voix de 0 à ~76 s, puis ~4 s de silence/outro (coucher de soleil).
- Aucun cut dur détecté (scene score > 0,3 = 0) : tout est animé en continu par morphing/caméra. Les changements de scène sont des fondus enchaînés et des mouvements de caméra, pas des coupes.

## Structure du récit (script ~248 mots, ~196 mots/min)
1. **Hook (0-4 s)** : problème concret du quotidien (« Si tu veux streamer Netflix sur un bateau au milieu de l'océan, tu as un problème »).
2. **Raisonnement en escalade** : « donc tu fais X » -> « mais ça crée Y » -> « donc tu fais Z ». Chaque phrase résout le problème de la précédente (satellite géostationnaire -> latence 0,5 s -> orbite basse -> le satellite bouge -> des milliers de satellites -> antenne à balayage électronique -> liaisons laser).
3. **Relance à ~59 s** : « Tu pourrais croire que c'est fini. Mais... » pour retenir l'attention.
4. **Chute (74-76 s)** : « Félicitations, tu viens de construire Starlink. » Le nom du sujet n'est révélé qu'à la fin (carte-titre « S T A R L I N K »).
- Phrases courtes (1,5 à 3 s), 1 idée par phrase, chiffres concrets (22 000 miles, 30 ms, 17 000 mph, 11 000+).
- Ton « tu » : le spectateur est le protagoniste (marqueur « YOU » sur les visuels).

## Visuel
- Fond bleu nuit quasi noir avec grille fine, vignette de style « blueprint/terminal ».
- Bandeau haut : tag vert monospace à gauche (« NETFLIX · MID-OCEAN »), étiquette grise espacée à droite (« QUIET PACKET »). Constant sur toute la vidéo.
- Cadre arrondi central (~y 160-675 sur 960) qui contient l'illustration ; deux ambiances : coucher de soleil dégradé orange/violet (scène du bateau) et espace/Terre sombre (scènes orbitales).
- Illustrations vectorielles/3D low-poly propres : Terre avec lumières de villes, satellite, fusée, antenne, bateau, téléphone.
- Annotations en pastilles : jaune (distances, « 22,236 mi »), bleu (« 340 mi »), vert (« THE INTERNET »), rouge (« SIGNAL LOST »), police monospace.
- Cartes de chiffres animées en fin de vidéo : 61 -> 6 782 -> 11 000+ (compteur), puis titre espacé.
- Légende de contexte en petit au-dessus de l'illustration (« Earth and orbits to scale · satellites enlarged »).
- Reflet flou de l'illustration sous le cadre (glow).

## Sous-titres
- Mot à mot / groupes de 1 à 3 mots, une seule ligne, centrés, bas du cadre (~y 745/960, sous l'illustration).
- Police sans-serif grasse blanche (type Inter Bold) sur boîte noire opaque avec fin liseré gris.
- Le texte change à chaque groupe (pas de karaoké), ponctuation conservée (« flat, »).

## Audio
- Voix off synthétique/neutre, claire, rythme soutenu et régulier, mono.
- Loudness -23,8 LUFS intégré (assez bas, LRA 3 LU), pas de musique forte repérée ; très peu d'ambiance.
- Pauses de ~0,3 s entre les phrases, synchronisées avec les changements de visuel.

## À reproduire pour Focal Cosmos
- Même squelette narratif : problème concret -> chaîne « donc... mais... donc » -> relance -> chute avec révélation.
- Même grammaire visuelle (cadre central + bandeau haut + sous-titres boîte noire) mais avec l'identité Focal Cosmos (logo infini, argent/bleu nuit) et des tags FR.
- Voix et sous-titres en français, 75-85 s, ~190 mots/min (~240-260 mots).
- Réutiliser un composant de sous-titres, de pastilles et de compteur dans HyperFrames (skills `hyperframes`, `hyperframes-registry`, `style-sampling`).
