module attributes {torch.debug_module_name = "simple"} {
  func.func @forward(%arg0: tensor<1x3x16x16xf32>) -> tensor<1x8x16x4xf32> {
    %0 = "tosa.const"() <{value = dense<1.000010e+00> : tensor<8x1x1xf32>}> : () -> tensor<8x1x1xf32>
    %1 = "tosa.const"() <{value = dense<[1, 0]> : tensor<2xi32>}> : () -> tensor<2xi32>
    %2 = "tosa.const"() <{value = dense<[0, 3, 1, 2]> : tensor<4xi32>}> : () -> tensor<4xi32>
    %3 = "tosa.const"() <{value = dense<[0, 2, 3, 1]> : tensor<4xi32>}> : () -> tensor<4xi32>
    %4 = "tosa.const"() <{value = dense<[-0.0717707872, -0.0423891321, 0.00969634484, -0.0271288622, -0.130245402, -0.150103226, -0.0827921405, -0.0530781448]> : tensor<8xf32>}> : () -> tensor<8xf32>
    %5 = "tosa.const"() <{value = dense<"0x2E068BBC77E9EF3CAC13F2BCF97143BE5C88E6BD7FF68C3D9BD4B2BD9867B0BDFC531E3DED3DD7BCF43ECD3DFCC2973D920C293E1755CC3BE81B3A3CE4C01F3E5EBB2DBE85570CBEF309EABDFEF7C4BC30CB82BD086004BE754D193D4DBA24BE1EECF03D5CB9B5BD46E6323ED4B2B9BB1DAFC93DA88EECBC01B615BDCA5501BD78EC9BBD27761D3EB53229BEE1BED53DD50506BEB66DAC3D7D06C73C083C283E871307BC58B2D3BD7A7C2D3E054D9ABD926C35BEBA8307BEF8A4E339B29AC33DDA5A353EC9D4A93A731935BE8C24D73D8ED6823D9728CBBDFC20423E8D12EE3D62A7A6BDA5E1A03DC5EDDDBB1C5728BD3A6748BD57E0BEBDEC4A2FBE2EB0CE3CAFFF293E7B0601BEBE1420BE364037BE7D1A77BD3AA8BA3D040312BEC7C382BCE65622BE64B6C43D78A108BE84E917BEB62453BD54EA233EB6CEFF3D45200D3ED2A9293ED477503D7D6B15BEE1F42DBDEE8CEBBDD143733DC479F23D45AE293D7ED732BE6528133E73D008BD3B5F233DD7BED33D8D7F2CBD244C833DB510EABDA6DC06BE6E57C6BD3BEB543D34AAF0BBF2A0093D9617303EB29C1FBE8C0598BDA1CE9D3DCC4A14BE9B15DC3D80422DBD9B04383E2B4D193EDBED71BD65D4133E5E282EBE601F25BD73068ABD87E782BD4510D43D104D2FBE3AF2D03DF7FCA3BDABB724BEF3A2CC3D4899DB3DA1F633BEE4D00CBEBFF58BBDE0EE07BE9BEA5B3D9EA68CBD6F2A823D153D57BD5D8C273D019BEDBD548B1D3E1D07233BC61E133D3A0BA73CFA0043BCC3A706BE64BE363EB992133B3F1C2BBE15ABD23D69A8CE3D1A0A3D3E7233073E1DD6C33DCF1A04BE301A233E97C70DBE68FB993CE2AEB93CB72EBF3D2E9DEF3D75BFB73DF26705BE010E1A3D9CDC6A3D4989BB3DE034E1BDC58E2BBDB7D7C53DA8C7DABD6370133E1DB47EBCCB8034BEB0FF8C3D7C7ED2BD0FA283BCCBE87ABD2F41DCBBA0603BBE8C75B43C4ED84E3D0956253E83C813BD8EBD83BD8F7E1F3E3ED0243EB8898B3C2ED043BEB76A17BEB68370BD80B8313D80B45B3C5EB0B6BDD400CF3DBF49273E914DC43DD3F713BEC0A442BEC8EDE63B7A24A73D7EAE173E0490013E33504B3D391B79BD2DC4993C1B69093E8ABFAC3D16700EBEAE02CF3D61AD26BE9B688BBDDA2735BB81A305BE689534BE33E42BBED8F137BBE01CDD3D4275D2BD46CCF3BDA9393DBD8B27423E13A9873D52BA703D"> : tensor<8x3x3x3xf32>}> : () -> tensor<8x3x3x3xf32>
    %6 = "tosa.const"() <{value = dense<[-0.132966399, -0.10632199, -6.313750e-02, 0.111462414, -0.0230877101, -2.71707773E-4, -0.102463722, -0.227972597]> : tensor<8xf32>}> : () -> tensor<8xf32>
    %7 = "tosa.const"() <{value = dense<"0xD4DA02BE9CFD59BE6050E1BDA260473EC08246BDA0E52DBEE8A9583D6C66593E0808E3BD18B16D3E968053BE8E01593E6A121E3E402946BD22457F3E88E26FBD3EAC34BEE47D67BEEE7D493E1013453DC853AB3D12A4063E28AA253DEA452ABE80FE62BB3E11443EC0B9C93BEC2387BDC084323C94D92FBEA413873D6EDD1CBEB22279BE50640D3EC090403DC6F33EBEA46A5CBEC06E5DBE946596BDE8E038BE94BD16BE6075A3BDCC97763E4C763F3EC0FC693D7CD2063EC42F743E72F601BEA8966DBE1052413D20EDEC3D96303B3E804CAFBDE01954BD2090B3BDF09C94BC12B378BE7A715BBE90862DBE2030773DDECB143E4E03633EDEBD00BE948483BDBECF0F3EC21506BED0A83BBE546BCC3D8AE619BE502E5F3DECB2513EB0A1C53C746BEEBDE682453EF09677BE98F9363E7C72143E2C3B9BBDC44AD5BD505F7EBD72417D3E084418BE10BB643E6837123D688A4ABD70E8713E00A0D0BA9038573D0C9AC6BDF4155F3E64F3C3BD30D01F3E940D2E3E1A55273E54724B3E980F9A3D40FF21BDAE684CBE14322E3EE65B1F3E188B8A3DE83D58BE086145BE6C40A73D8CCF853D940A443E50EE5FBEF0D6853DC08AD03DA0B0693E66453F3E98F7E9BD787D4C3E5C5D37BE2053023EE892933D585B283DF492E83DDA2F7F3EB054A53CC081983DFA5D493E5020E7BC60A8903CBCD9153E3891B93D90CCBDBCA0CB26BC"> : tensor<8x16xf32>}> : () -> tensor<8x16xf32>
    %8 = "tosa.const"() <{value = dense<[-0.121429406, 0.0909240693, 0.0867559984, 0.169947132]> : tensor<4xf32>}> : () -> tensor<4xf32>
    %9 = "tosa.const"() <{value = dense<[[0.0987183302, 0.29641974, -0.341286719, 0.168666959, 0.030892713, 0.211126029, -0.212056011, -0.0775878354], [-0.137849271, 1.364540e-01, -0.282808691, -0.25722453, 0.152626127, 0.061977107, 0.139302328, -0.25885573], [0.203331098, -0.339602977, -0.131707594, -0.195234984, 0.180179372, -0.154441521, 0.295544952, 0.219060048], [0.105150819, -0.199884921, 0.26574105, -0.22690931, -0.198123857, -0.0343345925, -0.0595564879, -0.174453765]]> : tensor<4x8xf32>}> : () -> tensor<4x8xf32>
    %10 = "tosa.transpose"(%arg0, %3) : (tensor<1x3x16x16xf32>, tensor<4xi32>) -> tensor<1x16x16x3xf32>
    %11 = "tosa.transpose"(%5, %3) : (tensor<8x3x3x3xf32>, tensor<4xi32>) -> tensor<8x3x3x3xf32>
    %12 = "tosa.conv2d"(%10, %11, %4) <{dilation = array<i64: 1, 1>, pad = array<i64: 1, 1, 1, 1>, stride = array<i64: 1, 1>}> : (tensor<1x16x16x3xf32>, tensor<8x3x3x3xf32>, tensor<8xf32>) -> tensor<1x16x16x8xf32>
    %13 = "tosa.transpose"(%12, %2) : (tensor<1x16x16x8xf32>, tensor<4xi32>) -> tensor<1x8x16x16xf32>
    %14 = "tosa.rsqrt"(%0) : (tensor<8x1x1xf32>) -> tensor<8x1x1xf32>
    %15 = "tosa.mul"(%13, %14) <{shift = 0 : i32}> : (tensor<1x8x16x16xf32>, tensor<8x1x1xf32>) -> tensor<1x8x16x16xf32>
    %16 = "tosa.clamp"(%15) <{max_fp = 3.40282347E+38 : f32, max_int = 2147483647 : i64, min_fp = 0.000000e+00 : f32, min_int = 0 : i64}> : (tensor<1x8x16x16xf32>) -> tensor<1x8x16x16xf32>
    %17 = "tosa.transpose"(%7, %1) : (tensor<8x16xf32>, tensor<2xi32>) -> tensor<16x8xf32>
    %18 = "tosa.reshape"(%16) <{new_shape = array<i64: 1, 128, 16>}> : (tensor<1x8x16x16xf32>) -> tensor<1x128x16xf32>
    %19 = "tosa.reshape"(%17) <{new_shape = array<i64: 1, 16, 8>}> : (tensor<16x8xf32>) -> tensor<1x16x8xf32>
    %20 = "tosa.matmul"(%18, %19) : (tensor<1x128x16xf32>, tensor<1x16x8xf32>) -> tensor<1x128x8xf32>
    %21 = "tosa.reshape"(%20) <{new_shape = array<i64: 1, 8, 16, 8>}> : (tensor<1x128x8xf32>) -> tensor<1x8x16x8xf32>
    %22 = "tosa.add"(%21, %6) : (tensor<1x8x16x8xf32>, tensor<8xf32>) -> tensor<1x8x16x8xf32>
    %23 = "tosa.clamp"(%22) <{max_fp = 3.40282347E+38 : f32, max_int = 2147483647 : i64, min_fp = 0.000000e+00 : f32, min_int = 0 : i64}> : (tensor<1x8x16x8xf32>) -> tensor<1x8x16x8xf32>
    %24 = "tosa.transpose"(%9, %1) : (tensor<4x8xf32>, tensor<2xi32>) -> tensor<8x4xf32>
    %25 = "tosa.reshape"(%23) <{new_shape = array<i64: 1, 128, 8>}> : (tensor<1x8x16x8xf32>) -> tensor<1x128x8xf32>
    %26 = "tosa.reshape"(%24) <{new_shape = array<i64: 1, 8, 4>}> : (tensor<8x4xf32>) -> tensor<1x8x4xf32>
    %27 = "tosa.matmul"(%25, %26) : (tensor<1x128x8xf32>, tensor<1x8x4xf32>) -> tensor<1x128x4xf32>
    %28 = "tosa.reshape"(%27) <{new_shape = array<i64: 1, 8, 16, 4>}> : (tensor<1x128x4xf32>) -> tensor<1x8x16x4xf32>
    %29 = "tosa.add"(%28, %8) : (tensor<1x8x16x4xf32>, tensor<4xf32>) -> tensor<1x8x16x4xf32>
    return %29 : tensor<1x8x16x4xf32>
  }
}

