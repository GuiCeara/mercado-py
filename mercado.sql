-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 18-Nov-2022 às 17:54
-- Versão do servidor: 5.7.36
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mercado`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `historico`
--

DROP TABLE IF EXISTS `historico`;
CREATE TABLE IF NOT EXISTS `historico` (
  `pedidoN` int(11) NOT NULL AUTO_INCREMENT,
  `fk_usuarios_usuario` varchar(200) NOT NULL,
  `nomeProduto` varchar(200) NOT NULL,
  `quantidadeTotal` int(11) NOT NULL,
  `precoTotal` double NOT NULL,
  `dataCompra` varchar(30) NOT NULL,
  PRIMARY KEY (`pedidoN`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `historico`
--

INSERT INTO `historico` (`pedidoN`, `fk_usuarios_usuario`, `nomeProduto`, `quantidadeTotal`, `precoTotal`, `dataCompra`) VALUES
(1, 'guilherme', 'Coca-Cola 2L', 4, 42, '2022-11-17 10:55:03.594023'),
(2, 'guilherme', 'Bolacha Tartaruga', 5, 12.5, '2022-11-17 10:56:35.092256'),
(3, 'guilherme', 'Coca-Cola 2L', 6, 63, '2022-11-17 11:02:18.172420'),
(4, 'guilherme', 'Creme de Avelã 1kg', 1, 50.36, '2022-11-17 11:28:15.289223'),
(5, 'admin', 'Coca-Cola 2L', 5, 52.5, '2022-11-17 11:29:45.062749');

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

DROP TABLE IF EXISTS `produtos`;
CREATE TABLE IF NOT EXISTS `produtos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(220) NOT NULL,
  `estoque` int(200) NOT NULL,
  `valor` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`id`, `nome`, `estoque`, `valor`) VALUES
(1, 'Arroz ', 10, 18.75),
(2, 'feijão', 5, 9.9),
(3, 'Farinha de Trigo', 5, 5.7),
(4, 'Farofa', 4, 4.5),
(5, 'Creme de Avelã 1kg', 2, 50.36),
(6, 'Bolacha Tartaruga', 7, 2.5),
(7, 'Coca-Cola 2L', 15, 10.5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario` varchar(200) NOT NULL,
  `senha` varchar(16) NOT NULL,
  PRIMARY KEY (`usuario`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `senha`) VALUES
('admin', 'admin123'),
('creator', 'creator123'),
('guilherme', 'gui123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
