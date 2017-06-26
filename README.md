# Festivals dominated by male acts, study shows, as Glastonbury begins

![](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/festivalfemalesgif.gif)

In June 2017 we [published an analysis of music festival data](http://www.bbc.co.uk/news/uk-england-40273193) which highlighted the scarcity of female headliners, the dominance of 20 acts which make up a quarter of all headline slots, how Glastonbury headliners are getting older, and the rise of pop and hip hop and decline of electronic and rock.

BBC England's data unit analysed more than 600 separate headline performances across 14 UK festivals. They were: Download, Reading/Leeds, T in the Park, V Festival, Isle of Wight, Bestival, Latitude, Wireless, Rewind, End of the Road, Cornbury, Boardmasters and Lovebox.

Festivals that were not defined around headline acts were excluded. These include Creamfields, Boomtown Fair and Womad. Fairport's Cropredy Convention was also excluded as it is traditionally headlined by its organisers.

We selected festivals using Festival Insights, a publication that runs the UK Festival Awards and publishes a list of the top 250 music festivals in Europe. The Spotify API was used to obtain data on genre, popularity, and related artists, and data compilation and analysis was done with both Python and R.

## Unpublished: network analysis

Not included in the final article was a network analysis of the festival headliners and related artists. You can [see a network diagram showing just headliners here](https://fusiontables.googleusercontent.com/embedviz?containerId=googft-gviz-canvas&viz=GVIZ&t=GRAPH&gc=false&gd=false&sdb=1&rmax=100000&q=select+col3,+col4,+col5+from+18D_okJHIQ0E_Gqfz-SEFbijoIXxSSzZfkDU1PbMK&qrs=+where+col3+%3E%3D+&qre=+and+col3+%3C%3D+&qe&uiversion=2&state={%22ps%22:%221_0_55_-c_9_5b_-3t_7_6q_-3e_4_42_-1j_e_6r_-44_5_42_8_3_6f_-1q_a_5m_-50_1_4o_j_b_5s_-4c_h_65_-31_2_4r_-12_s_2w_a_f_2q_-x_c_7d_-37_g_3g_-y_k_64_-3s_p_3g_o_11_6h_-2e_w_3i_-a_x_46_-c_i_6c_-4q_v_31_-1g_l_8a_1m_1b_3m_-6m_1c_3a_-60_8_5h_-35_o_8i_x_1e_48_-5v_15_1l_-3f_1x_5t_-1u_12_5_-33_1l_48_-6u_q_8o_27_t_2b_-k_1f_35_-6w_10_75_-2b_1d_3f_-7d_m_7r_21_1j_5h_-2m_1i_2l_-6n_n_8x_1e_1h_4i_-6g_r_4l_-4j_2l_41_-z_27_18_-2m_28_7m_-9_3l_3v_-p_34_5y_-s_1m_3f_7_1n_30_-e_26_1u_-3w_z_5d_-1p_1t_8c_-t_1k_3y_-7d_1g_21_-11_d_6v_-4r_j_7i_-41_13_i_-3u_16_2v_-44_1o_2e_0_2r_8q_9_18_73_-2q_2d_g_-25_2k_5m_-13_1y_1i_-5r_2s_89_-3_17_2s_-4h_y_40_y_1a_-1_-3x_3k_5b_m_36_-o_-30_33_69_-e_2j_2r_-2u_14_a_-3i_1w_7n_-x_2b_7r_14_2v_7i_-l_2g_1l_-1l_2n_4_-y_19_2z_-3b_21_28_-25_2w_7k_-18_3u_26_-1f_2m_10_-3v_3c_-4_-8_4d_5s_-2c_u_48_-3q_1q_9b_r_2i_2x_-6c_31_-v_-2f_25_2i_-2g_5d_6e_-5_6_5v_l_24_1n_-6c_43_21_-6_2h_h_-1c_30_w_-p_3s_2e_-1k_2x_-z_x_39_7z_o_1r_2a_-4e_1z_1h_-4e_22_-78_3d_35_9j_-3_2f_4d_-44_4v_1e_-41_20_n_-5u_2a_7s_30_3i_-17_l_4e_20_-1q_2o_f_6_2q_4e_-o_2y_-1f_-3_32_6q_-7_3h_-1j_-3d_2c_6v_-y_2e_z_-4j_2t_78_-z_1u_4x_4_37_-12_-r_3j_-7l_29_4s_-2l_6l_64_2t_-3r_1p_9i_18_1s_2p_-52_1v_93_4_23_-6k_2t_2u_79_-1b_3f_-h_10_5b_75_1i_3d_-19_8_40_-1x_1v_4x_8d_39_2p_29_-3e_3b_8t_-s_47_v_l_4b_2o_-9_66_4d_-26_4r_-1s_7c_5w_52_-1f_4h_-3x_5y_3a_-q_-21_3q_6a_1s_3t_90_3f_3z_77_f_44_11_-25_45_q_-a_4o_-2t_5i_4w_2e_-41_6g_6j_-n_4j_-1m_1d_29_26_-4w_2z_9d_-g_3e_-h_-3j_48_-4i_-72_4f_-1i_67_5c_6w_1q_3m_3_-5c_4q_-39_75_%22,%22cx%22:274.7886358660946,%22cy%22:-81.89398949875394,%22sw%22:1918.3229499293088,%22sh%22:772.9788593423319,%22z%22:-0.7480141739809658}&gco_forceIFrame=true&gco_hasLabelsColumn=true&width=1000&height=600) and o[ne showing headliners and all artists that Spotify identifies as 'related' here](https://fusiontables.googleusercontent.com/embedviz?containerId=googft-gviz-canvas&viz=GVIZ&t=GRAPH&gc=true&gd=true&sdb=1&rmax=100000&q=select+col0,+col1,+col2+from+1SXjcZA2MMoit2yb4_4_5xawTMFhuzCq2jNquqGdO&qrs=+where+col0+%3E%3D+&qre=+and+col0+%3C%3D+&qe&uiversion=2&state=%7B%22ps%22:%221_5j_-5s_4j_5c_-4a_3b_5y_-6p_1f_hv_-5f_p_64_-60_13_hl_-av_-2w_5m_-4n_5b_hz_-5e_-9_5h_-4s_3n_m6_-6g_3b_5g_-56_4v_hx_-7d_1k_2o_-31_5e_1p_-bp_-2x_5n_-3r_5e_5p_-43_4v_hw_-5x_7_lx_-73_2a_m0_-5t_2d_5l_-49_5z_5b_-3n_3c_hy_-6t_r_2z_-h_2z_m4_-42_3x_5r_-4t_5z_i4_-6j_1y_2l_-31_4u_ef_-ak_-21_5a_-3q_4f_au_-16_1r_lv_-6y_2z_i0_-6b_-e_lz_-4t_47_1gb_-2a_1r_95_-2g_-2e_2m_-2x_65_61_-5v_3c_qx_-68_5b_9a_-38_-27_98_-28_-35_33_-1a_33_ew_-b5_-1x_1g6_-6o_-x_s4_-ab_-3f_5u_-5g_1d_qf_-8r_-2d_53_-1o_19_u8_-6c_m_94_-1x_-2p_hn_-9k_-2b_18c_-69_2q_m3_-56_30_5f_-39_3y_lw_-6q_40_5t_-5a_1z_1g5_-7c_-i_w3_-21_-3x_1g_-be_-2g_69_-5p_1q_9y_-5z_5t_a5_-3i_6a_m5_-8q_9_1b_-8m_-1p_9c_-39_-32_3i_-av_-3p_1m8_-79_4_iq_-cu_-2z_s3_-a8_-2t_4v_-o_3o_3q_-f_23_hj_-9e_-s_y9_-3l_-a_ae_-x_-3x_e4_-5d_5k_4x_-2k_3n_w6_-1k_-38_1k_-by_-2e_5x_-64_1n_8z_-2s_1f_lu_-74_3e_9k_-3n_-2o_tf_-bz_-3r_6d_-4e_v_1ki_-32_j_hi_-9y_-21_9b_-2m_-3s_bb_-1q_k_6n_-2h_-17_9m_-35_-3s_qy_-6p_57_ip_-cf_-3h_k9_-ag_-1j_51_-13_14_bl_k_3j_1fr_-be_-3t_u6_-4y_1m_hs_-cm_-20_56_p_2n_8p_-40_1k_1uy_-4g_c_yc_-2a_1_159_-2v_-3c_iv_-hd_-g_5q_-4r_4n_i2_-7a_l_1l2_-9o_-1k_1m2_-5d_3k_112_-3a_17_1m5_-34_1z_tg_-84_-1f_m_-7q_-4j_58_7_22_q5_-8r_-18_6m_-3u_-1k_h8_-4d_4c_hf_-5h_43_ox_-1m_-1k_6r_-2w_-7_n_-6p_-3w_i1_-6n_4_6e_-31_-v_2p_-2f_4v_hh_-au_-1c_6k_-3i_s_kv_-l_s_i3_-4i_-6_8v_-2p_v_2k_-1n_4n_j1_-gs_i_hb_-3p_4v_yu_-59_4g_t_-6w_-5b_q8_-86_-32_id_-p_4k_bj_6_2y_bk_f_45_m2_-7c_4t_11d_-9t_-35_es_-ap_-w_23_-7p_5y_57_-1u_2c_pd_-7r_4r_i9_-23_67_ed_-by_-17_cu_-5e_6i_15c_-57_-2p_%22,%22cx%22:65.2156039482535,%22cy%22:-2.672647037986948,%22sw%22:2149.15161378806,%22sh%22:789.6321097850513,%22z%22:-0.4993180324487124%7D&gco_forceIFrame=true&gco_hasLabelsColumn=true&width=1500&height=900). 

The network analysis shows headliners clustered with others that are considered 'related' by Spotify, and the size of each node reflects the numbers of other headliners that are related to that artist. An artist like Razorlight, then, is shown as more 'typical' of a festival headliner (large node, central position) than a peripheral artist like The Black Eyed Peas (only connected to one other headliner, and one the periphery of the network)

Likewise the network analysis shows that the Britpop cluster (centre right) features more heavily among headliners than 80s artists (upper right), and artists connecting both clusters include The Cure and New Order. You can see who connects other clusters in a similar way.

![](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/festival_networkanalysis.png)

## Get the data

* [CSV: Headliners for each festival, including demographic data](https://github.com/BBC-Data-Unit/music-festivals/blob/master/festival_headliners.csv)
* [Excel spreadsheet: headliner demographics summary tables](https://github.com/BBC-Data-Unit/music-festivals/blob/master/festivaldata-withcalcs.xlsx)
* [CSV: Headliner IDs, names, related artists, top tracks, popularity, from Spotify API](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotifydata.csv)
* [CSV: Headliners by festival with Spotify genres](https://github.com/BBC-Data-Unit/music-festivals/blob/master/appearance_plus_genres.csv)
* [CSV: Genre frequency count](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/genrecount.csv)
* [CSV: Genre count times appearances](https://github.com/BBC-Data-Unit/music-festivals/blob/master/genrecount_x_appearances.csv)
* [CSV: Relationships between artists](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/relationships_between_artists.csv) - includes non-headliners
* [CSV: Relationships between artists - headliners only](https://github.com/BBC-Data-Unit/music-festivals/blob/master/relationships_headlinersonly.csv)
* [Spotify IDs and names for festival headliners and related artists](https://github.com/BBC-Data-Unit/music-festivals/blob/master/artistidlookup.csv) - related artists include non-headliners
* [CSV: MusicBrainz IDs and Spotify IDs for headliners](https://github.com/BBC-Data-Unit/music-festivals/blob/master/headliners_musicbrainzids.csv)

## Visualisation

![](https://ichef.bbci.co.uk/news/624/cpsprodpb/849C/production/_96484933_chart_mostpopular_glasto.png)

* Line chart: Percentage of headline acts by gender each year
* Bar chart: Acts with the most festival headline appearances
* Multiple bar chart: Is rock music in decline? Genre tags associated with headline acts (%)
* Bar chart: How Glastonbury headliners have been getting older

## Multimedia 

* Video: UK festival line-ups dominated by male headliners

## Analysis and code

* [Python scraper which uses the Spotify API to fetch details on a list of headline acts](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotifyscraper.py)
* [How to do the same thing using a scraper in R](https://github.com/BBC-Data-Unit/music-festivals/blob/master/using_spotify_api.Rmd)
* [Analysing genre using R](https://github.com/BBC-Data-Unit/music-festivals/blob/master/analysingSpotifyGenre.Rmd)
* [Creating data on related artists for a network analysis in R](https://github.com/BBC-Data-Unit/music-festivals/blob/master/SpotifyNetworkAnalysis.Rmd)
* [R script for converting list column into popularity lookup table](https://github.com/BBC-Data-Unit/music-festivals/blob/master/createlookup.R)
* [R script for converting table into data that can be used for network analysis](https://github.com/BBC-Data-Unit/music-festivals/blob/master/createnetworktable.R)
* All these scripts can be used as part of the [R project](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotify.Rproj)

## Related stories

The Times also did an analysis of data relating to music festivals in two articles and identified similar trends: [Four-fifths of acts booked at major festivals are male] and [Will we rock you? How UK festivals have changed their tune](https://www.thetimes.co.uk/edition/times2/will-we-rock-you-how-uk-festivals-have-changed-their-tune-jrpqnfkfp) explored gender and genre respctively. The sample was slightly different: 8 festivals over 10 years, and main stage acts (we looked at headliners at 14 festivals over 46 years).
