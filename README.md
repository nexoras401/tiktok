# Loja mobile e painel administrativo

Protótipo educativo independente de e-commerce, sem vínculo com o TikTok. Inclui catálogo com fotos incorporadas, páginas de produto, carrinho, cupom configurável, ofertas relâmpago e painel administrativo separado.

## Arquivos

- `outputs/prototipo-loja.html`: loja.
- `outputs/admin.html`: painel administrativo.
- `outputs/servidor-local.py`: servidor local em Python, sem dependências adicionais.

## Executar localmente

Com Python 3 instalado, execute na raiz do repositório:

```sh
python outputs/servidor-local.py
```

O painel será aberto no navegador. Endereços:

- Loja: http://127.0.0.1:8765/prototipo-loja.html
- Admin: http://127.0.0.1:8765/admin.html

Use as duas páginas na mesma origem para compartilhar os dados do navegador. Recarregue a loja após editar no admin. Dados anteriores de páginas abertas como `file://` não migram automaticamente.

## Recursos

- Cadastro e edição de produtos, fotos e avaliações de exemplo.
- Dashboard com pedidos de teste registrados neste navegador.
- Campanha configurável com nome, percentual, código, descrição e botão.
- Ofertas relâmpago com duração e contador persistente local.
- Recomendações, pesquisa, categorias e favoritos.

## Estado do projeto

Não há autenticação, banco de dados remoto ou integração de pagamentos reais. Dados editados, pedidos e configurações ficam no `localStorage`, não neste repositório. Separar a página administrativa não a protege contra acesso. O servidor fornecido escuta somente em `127.0.0.1` e serve para desenvolvimento local.

Antes de operar uma loja real, são necessários identidade comercial própria, catálogo e avaliações verdadeiros, backend com validação de preços e pedidos, autenticação administrativa e integração com um provedor de pagamentos.

## Créditos das fotos dos 30 produtos adicionais

As imagens dos produtos de id 25 a 54 vêm do [Wikimedia Commons](https://commons.wikimedia.org/), foram reduzidas para 650×650 com fundo branco e incorporadas em base64. Cada produto guarda o endereço do arquivo em `source`. Licenças Creative Commons exigem atribuição, registrada abaixo. A presença das fotos e marcas não implica parceria ou autorização comercial.

| Produto | Arquivo | Licença | Autor |
| --- | --- | --- | --- |
| Aspirador Portátil Sem Fio | [Dyson V6 Trigger handheld vacuum.jpg](https://commons.wikimedia.org/wiki/File:Dyson_V6_Trigger_handheld_vacuum.jpg) | CC BY 2.0 | Your Best Digs |
| Bolsa feminina compacta com Alça | [Flower Print Purse.jpg](https://commons.wikimedia.org/wiki/File:Flower_Print_Purse.jpg) | CC BY-SA 4.0 | Gaurav Dhwaj Khadka |
| Bolsa Transversal de Lona com Alça | [Shoulder bag MET DP-14863-025.jpg](https://commons.wikimedia.org/wiki/File:Shoulder_bag_MET_DP-14863-025.jpg) | CC0 | Wikimedia Commons |
| Caixa de Som Bluetooth Portátil | [Bluetooth speaker NBY-18 P8041745.jpg](https://commons.wikimedia.org/wiki/File:Bluetooth_speaker_NBY-18_P8041745.jpg) | CC BY-SA 4.0 | Alexxx1979 |
| Câmera de Segurança Wi-Fi Full HD | [Wifi Security camera - Tapo C100.jpg](https://commons.wikimedia.org/wiki/File:Wifi_Security_camera_-_Tapo_C100.jpg) | CC BY-SA 4.0 | Vis M |
| Carregador Rápido GaN 30W | [Lazos GaN Charger 30W L-AC-G30.jpg](https://commons.wikimedia.org/wiki/File:Lazos_GaN_Charger_30W_L-AC-G30.jpg) | CC BY-SA 4.0 | Qurren |
| Carteira Slim RFID em Couro | [I-CLIP Slim Wallet 03.jpg](https://commons.wikimedia.org/wiki/File:I-CLIP_Slim_Wallet_03.jpg) | CC BY 4.0 | www.kartenetui.info |
| Escova Secadora 2 em 1 com Íons | [HITACHI HAIR DRYER HD-1650.jpg](https://commons.wikimedia.org/wiki/File:HITACHI_HAIR_DRYER_HD-1650.jpg) | CC BY-SA 4.0 | Dinkun Chen |
| Fone Bluetooth Esportivo com Gancho | [Sport Wireless Headphones Toxxel.jpg](https://commons.wikimedia.org/wiki/File:Sport_Wireless_Headphones_Toxxel.jpg) | CC BY-SA 4.0 | Juan93sosa |
| Fone Bluetooth Pro TWS com Estojo | [Powerbeats Pro 2 Charging Case - 1.jpg](https://commons.wikimedia.org/wiki/File:Powerbeats_Pro_2_Charging_Case_-_1.jpg) | CC BY-SA 4.0 | Kyu3a |
| Garrafa Térmica Inox 500ml | [Thermos-JOJ-150-Mint 02.jpg](https://commons.wikimedia.org/wiki/File:Thermos-JOJ-150-Mint_02.jpg) | CC BY 4.0 | RuinDig/Yuki Uchida |
| Kit 12 Pincéis de Maquiagem | [Full Set of Make Up Brushes on Blue & White Background - 50922295762.jpg](https://commons.wikimedia.org/wiki/File:Full_Set_of_Make_Up_Brushes_on_Blue_%26_White_Background_-_50922295762.jpg) | CC BY 2.0 | geehairimages |
| Kit Skincare 5 Passos | [Skin Care Set.jpg](https://commons.wikimedia.org/wiki/File:Skin_Care_Set.jpg) | CC BY-SA 4.0 | WGW2007 |
| Luminária LED RGB 5m com Controle | [LED light strip.jpg](https://commons.wikimedia.org/wiki/File:LED_light_strip.jpg) | CC BY-SA 4.0 | Maksym Kozlenko |
| Máscara Capilar Nutritiva | [Conditioner - Hair treatment.jpg](https://commons.wikimedia.org/wiki/File:Conditioner_-_Hair_treatment.jpg) | CC BY 2.0 | geehairimages |
| Massageador Elétrico Portátil | [Using a percution massage gun to do a foot massage.jpg](https://commons.wikimedia.org/wiki/File:Using_a_percution_massage_gun_to_do_a_foot_massage.jpg) | CC BY-SA 3.0 | Best For My Feet |
| Mini Impressora Térmica Bluetooth | [Niimbot D11 Thermal printers.png](https://commons.wikimedia.org/wiki/File:Niimbot_D11_Thermal_printers.png) | CC BY-SA 4.0 | Niimbot D11 Thermal printers |
| Mini Liquidificador Portátil USB | [Techwood mini blender, Oude Pekela (2019) 01.jpg](https://commons.wikimedia.org/wiki/File:Techwood_mini_blender,_Oude_Pekela_(2019)_01.jpg) | CC BY-SA 4.0 | Donald Trung Quoc Don (Chữ Hán: 徵國單) - Wikimedia Commons - © CC BY-SA 4.0 Intern |
| Mini Projetor Portátil Full HD 1080P | [Optoma Pico 301 20160315.jpg](https://commons.wikimedia.org/wiki/File:Optoma_Pico_301_20160315.jpg) | CC BY-SA 4.0 | Dehani bandara |
| Mochila Antifurto com Porta USB | [CitiBike Angel backpack 2024 jeh.jpg](https://commons.wikimedia.org/wiki/File:CitiBike_Angel_backpack_2024_jeh.jpg) | CC BY-SA 4.0 | Jim.henderson |
| Modelador de Cabelo Cerâmico | [Hair straightener TTH2510 by Tescom (2015-09-19).JPG](https://commons.wikimedia.org/wiki/File:Hair_straightener_TTH2510_by_Tescom_(2015-09-19).JPG) | CC BY-SA 4.0 | Lombroso |
| Óculos de Sol Polarizado UV400 | [Polarized sunglasses (2026).jpg](https://commons.wikimedia.org/wiki/File:Polarized_sunglasses_(2026).jpg) | CC BY-SA 4.0 | Gpkp |
| Organizador Empilhável para Casa | [Itoki Organizer.jpg](https://commons.wikimedia.org/wiki/File:Itoki_Organizer.jpg) | CC BY-SA 4.0 | Mr.ちゅらさん |
| Power Bank 20.000mAh Carga Rápida | [Mi50WPowerBank20000mAhXiaomi20240823000.jpg](https://commons.wikimedia.org/wiki/File:Mi50WPowerBank20000mAhXiaomi20240823000.jpg) | CC BY-SA 4.0 | OnionBulb |
| Ring Light 26cm com Tripé | [Ring Light 25280737679.jpg](https://commons.wikimedia.org/wiki/File:Ring_Light_25280737679.jpg) | CC0 | Serhan Meewisse |
| Smartwatch Fit à Prova d’Água | [Huawei Smartwatch Fit 2.jpg](https://commons.wikimedia.org/wiki/File:Huawei_Smartwatch_Fit_2.jpg) | CC BY-SA 4.0 | D Eaketts |
| Suporte para Celular com Tripé Flexível | [Mini tripod and phone holder.jpg](https://commons.wikimedia.org/wiki/File:Mini_tripod_and_phone_holder.jpg) | CC BY-SA 4.0 | ChimaBee |
| Teclado e Mouse Sem Fio Recarregável | [Wireless computer keyboard with mouse an USB receiver.jpg](https://commons.wikimedia.org/wiki/File:Wireless_computer_keyboard_with_mouse_an_USB_receiver.jpg) | CC BY-SA 4.0 | Andreas Schwarzkopf |
| Umidificador Ultrassônico de Mesa | [Ultrasonic humidifier.jpg](https://commons.wikimedia.org/wiki/File:Ultrasonic_humidifier.jpg) | Public domain | MaxSem |
| Ventilador Portátil Recarregável | [Battery-powered electric fan on a white background at home.jpg](https://commons.wikimedia.org/wiki/File:Battery-powered_electric_fan_on_a_white_background_at_home.jpg) | CC BY-SA 4.0 | Curpharar |

Fotos do catálogo inicial: [DummyJSON](https://dummyjson.com/docs/products). A presença das fotos e marcas não implica parceria ou autorização comercial. Não foi atribuída uma licença de redistribuição a esses materiais de terceiros.
